from fastapi import FastAPI, Depends, HTTPException, Header, UploadFile, File
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import subprocess
import os
import uuid
import json
import time
import asyncio
from pathlib import Path

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
    timeout: int = 60
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
            req.cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=req.cwd,
            env=env,
        )
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(), timeout=req.timeout
        )
        return ExecResponse(
            exit_code=proc.returncode or 0,
            stdout=stdout.decode("utf-8", errors="replace"),
            stderr=stderr.decode("utf-8", errors="replace"),
            duration=time.time() - start,
        )
    except asyncio.TimeoutError:
        proc.kill()
        return ExecResponse(
            exit_code=-1,
            stdout="",
            stderr=f"Command timed out after {req.timeout}s",
            duration=time.time() - start,
        )

@app.post("/api/upload")
async def upload_file(
    path: str,
    file: UploadFile = File(...),
    token=Depends(verify_token),
):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    content = await file.read()
    target.write_bytes(content)
    return {"path": str(target), "size": len(content)}

@app.get("/api/download")
async def download_file(path: str, token=Depends(verify_token)):
    from fastapi.responses import FileResponse
    target = Path(path)
    if not target.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(target), filename=target.name)

@app.get("/api/logs")
async def get_logs(service: str = "", lines: int = 50, token=Depends(verify_token)):
    cmd = f"docker-compose -f /workspace/docker-compose.new.yml logs --tail={lines}"
    if service:
        cmd += f" {service}"
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    return {"logs": stdout.decode("utf-8", errors="replace")}
