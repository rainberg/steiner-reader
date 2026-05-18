#!/bin/bash
set -e

echo "=== Steiner Reader 部署脚本 ==="
echo ""

# 检查是否在正确目录
if [ ! -f "docker-compose.new.yml" ]; then
    echo "错误: 请在 /workspace 目录运行此脚本"
    exit 1
fi

# 创建网络（如果不存在）
echo "[1/6] 检查 Docker 网络..."
docker network inspect steiner-network >/dev/null 2>&1 || docker network create steiner-network

# 停止旧服务
echo "[2/6] 停止旧服务..."
docker-compose down 2>/dev/null || true

# 构建新前端
echo "[3/6] 构建新前端..."
docker build -t frontend-new ./frontend-new

# 启动所有服务（使用新配置）
echo "[4/6] 启动所有服务..."
docker-compose -f docker-compose.new.yml up -d

# 等待服务启动
echo "[5/6] 等待服务就绪..."
sleep 5

# 健康检查
echo "[6/6] 健康检查..."
if curl -s http://localhost/health >/dev/null 2>&1; then
    echo "✅ 后端服务正常"
else
    echo "⚠️ 后端服务可能未就绪，请检查日志: docker-compose -f docker-compose.new.yml logs backend"
fi

echo ""
echo "=== 部署完成 ==="
echo ""
echo "访问地址:"
echo "  - 老前端: http://your-domain/"
echo "  - 新前端: http://your-domain/v2/"
echo ""
echo "回退命令:"
echo "  docker-compose -f docker-compose.new.yml down"
echo "  docker-compose up -d"
echo ""
echo "查看日志:"
echo "  docker-compose -f docker-compose.new.yml logs -f"
