#!/bin/bash
set -e

echo "╔══════════════════════════════════════════════════════╗"
echo "║   Steiner Reader 远程开发环境 - 一键部署脚本        ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

WORKSPACE="/workspace"
cd "$WORKSPACE" 2>/dev/null || { echo "错误: $WORKSPACE 不存在"; exit 1; }

# 检查 Docker
if ! command -v docker &>/dev/null; then
    echo "[0/7] 安装 Docker..."
    curl -fsSL https://get.docker.com | sh
    systemctl start docker
    systemctl enable docker
fi

# 检查 docker-compose
if ! command -v docker-compose &>/dev/null && ! docker compose version &>/dev/null; then
    echo "[0/7] 安装 docker-compose..."
    curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi

echo "[1/7] 创建 Docker 网络..."
docker network inspect steiner-network >/dev/null 2>&1 || docker network create steiner-network

echo "[2/7] 生成安全令牌..."
REMOTE_API_TOKEN=$(openssl rand -hex 32)
CODE_SERVER_PASSWORD=$(openssl rand -hex 16)

echo "[3/7] 创建 .env 文件..."
cat > "$WORKSPACE/.env" << EOF
REMOTE_API_TOKEN=$REMOTE_API_TOKEN
CODE_SERVER_PASSWORD=$CODE_SERVER_PASSWORD
EOF

echo "[4/7] 停止旧服务..."
docker-compose down 2>/dev/null || true

echo "[5/7] 构建并启动所有服务..."
docker-compose -f docker-compose.prod.yml up -d --build 2>&1

echo "[6/7] 等待服务就绪..."
sleep 10

echo "[7/7] 健康检查..."
HEALTH_OK=false
for i in $(seq 1 6); do
    if curl -s http://localhost/dev/api/status 2>/dev/null | grep -q "ok"; then
        HEALTH_OK=true
        break
    fi
    echo "  等待中... ($i/6)"
    sleep 5
done

echo ""
echo "╔══════════════════════════════════════════════════════╗"
if [ "$HEALTH_OK" = true ]; then
    echo "║  ✅ 部署成功！                                      ║"
else
    echo "║  ⚠️  部分服务可能需要更多时间启动                     ║"
    echo "║  请检查: docker-compose -f docker-compose.prod.yml logs ║"
fi
echo "╚══════════════════════════════════════════════════════╝"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  访问地址:"
echo "  ├─ 老前端:    https://steiner.3mudi.com/"
echo "  ├─ 新前端:    https://steiner.3mudi.com/v2/"
echo "  ├─ Web IDE:   https://steiner.3mudi.com/dev/ide/"
echo "  └─ 远程 API:  https://steiner.3mudi.com/dev/api/status"
echo ""
echo "  安全令牌 (请妥善保存):"
echo "  ├─ Remote API Token:  $REMOTE_API_TOKEN"
echo "  └─ Code Server 密码:  $CODE_SERVER_PASSWORD"
echo ""
echo "  令牌已保存到: $WORKSPACE/.env"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
