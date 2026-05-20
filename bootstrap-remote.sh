#!/bin/bash
set -e
echo "=== Steiner Remote API 引导安装 ==="
echo ""

# 生成令牌
TOKEN=$(openssl rand -hex 32 2>/dev/null || head -c 32 /dev/urandom | xxd -p)
echo "生成的 API Token: $TOKEN"
echo ""

# 创建 remote-api 目录
mkdir -p /workspace/remote-dev

# 写入 main.py
cat > /workspace/remote-dev/main.py << 'PYEOF'
from fastapi import FastAPI, Depends, HTTPException, Header, UploadFile, File
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import subprocess, os, time, asyncio
from pathlib import Path
from fastapi.responses import FileResponse

security = HTTPBearer()
API_TOKEN = os.environ.get("REMOTE_API_TOKEN", "")

app = FastAPI(title="Steiner Remote Dev API")

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return credentials

class ExecRequest(BaseModel):
    cmd: str
    cwd: str | None = None
    timeout: int = 120
    env: dict | None = None

class ExecResponse(BaseModel):
    exit_code: int
    stdout: str
    stderr: str
    duration: float

@app.get("/api/status")
async def status():
    return {"status": "ok", "timestamp": time.time()}

@app.post("/api/exec", response_model=ExecResponse)
async def exec_command(req: ExecRequest, token=Depends(verify_token)):
    start = time.time()
    env = os.environ.copy()
    if req.env:
        env.update(req.env)
    try:
        proc = await asyncio.create_subprocess_shell(
            req.cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
            cwd=req.cwd, env=env,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=req.timeout)
        return ExecResponse(exit_code=proc.returncode or 0, stdout=stdout.decode("utf-8", errors="replace"), stderr=stderr.decode("utf-8", errors="replace"), duration=time.time() - start)
    except asyncio.TimeoutError:
        proc.kill()
        return ExecResponse(exit_code=-1, stdout="", stderr=f"Timeout after {req.timeout}s", duration=time.time() - start)

@app.post("/api/upload")
async def upload_file(path: str, file: UploadFile = File(...), token=Depends(verify_token)):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    content = await file.read()
    target.write_bytes(content)
    return {"path": str(target), "size": len(content)}

@app.get("/api/download")
async def download_file(path: str, token=Depends(verify_token)):
    target = Path(path)
    if not target.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(target), filename=target.name)

@app.get("/api/logs")
async def get_logs(service: str = "", lines: int = 50, token=Depends(verify_token)):
    cmd = f"docker-compose -f /workspace/docker-compose.prod.yml logs --tail={lines}"
    if service:
        cmd += f" {service}"
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, _ = await proc.communicate()
    return {"logs": stdout.decode("utf-8", errors="replace")}
PYEOF

# 写入 Dockerfile
cat > /workspace/remote-dev/Dockerfile << 'DEOF'
FROM python:3.12-slim
WORKDIR /app
COPY main.py .
RUN pip install --no-cache-dir fastapi uvicorn python-multipart
EXPOSE 9000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
DEOF

# 创建 Docker 网络
docker network inspect steiner-network >/dev/null 2>&1 || docker network create steiner-network

# 构建 remote-api 镜像
echo "构建 remote-api 镜像..."
docker build -t steiner-remote-api /workspace/remote-dev/

# 启动 remote-api 容器
echo "启动 remote-api 容器..."
docker rm -f steiner-remote-api 2>/dev/null || true
docker run -d \
  --name steiner-remote-api \
  --network steiner-network \
  -e REMOTE_API_TOKEN=$TOKEN \
  -v /workspace:/workspace \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --restart unless-stopped \
  steiner-remote-api

# 等待启动
sleep 3

# 验证
if docker exec steiner-remote-api curl -s http://localhost:9000/api/status 2>/dev/null | grep -q "ok"; then
    echo ""
    echo "✅ Remote API 启动成功！"
else
    echo ""
    echo "⚠️ Remote API 可能需要几秒启动..."
    echo "   检查: docker logs steiner-remote-api"
fi

# 更新 nginx 配置添加 /dev/ 路由
echo ""
echo "更新 Nginx 配置..."
if [ -f /workspace/nginx.conf ]; then
    cp /workspace/nginx.conf /workspace/nginx.conf.backup.$(date +%s)
    if ! grep -q "remote-api" /workspace/nginx.conf; then
        sed -i '/upstream backend {/i\upstream remote_api {\n    server steiner-remote-api:9000;\n}\n' /workspace/nginx.conf
        sed -i '/location \/api\//i\    # Remote Dev API\n    location /dev/api/ {\n        proxy_pass http://remote_api/api/;\n        proxy_set_header Host $host;\n        proxy_set_header X-Real-IP $remote_addr;\n        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n        proxy_set_header X-Forwarded-Proto $scheme;\n        proxy_read_timeout 120s;\n    }\n' /workspace/nginx.conf
    fi
    # 重载 nginx
    docker exec $(docker ps -q --filter "ancestor=nginx:alpine" | head -1) nginx -s reload 2>/dev/null || echo "注意: 需要手动重载 nginx"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✅ 引导完成！"
echo ""
echo "  Remote API Token (请保存并告诉我):"
echo "  $TOKEN"
echo ""
echo "  测试命令:"
echo "  curl -H 'Authorization: Bearer $TOKEN' http://localhost:9000/api/status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
