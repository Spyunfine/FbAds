# FB Ads Parser — MVP (Block 1: Infrastructure)

Этот пакет поднимает инфраструктуру: PostgreSQL, Redis, MinIO и Backend (FastAPI).

## Запуск
1. Скопируйте `.env` из шаблона:
   ```bash
   cp infra/.env.example infra/.env
   ```

2. Поднимите окружение:
   ```bash
   docker-compose -f infra/docker-compose.yml up --build
   ```

3. Проверьте API-здоровье:
   - http://localhost:8000/health  → `{"status":"ok"}`
   - MinIO консоль: http://localhost:9001 (логин/пароль из `.env`)
   - PostgreSQL: порт 5432
   - Redis: порт 6379

## Структура
```
fb-ads-parser/
  backend/
    app/
      main.py          # FastAPI (health-check)
    Dockerfile
    requirements.txt
  infra/
    docker-compose.yml
    .env.example
  README.md
```
