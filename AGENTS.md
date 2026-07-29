# Финансовый менеджер

Stack: Python Flask + HTML/CSS/JS (vanilla, single-page)

## Структура

- `index.html` — фронт: кредиты, календарь платежей, модалки
- `server.py` — API: `GET/POST /api/data`, отдача статики, порт из `$PORT`
- `data.json` — данные на диске (в .gitignore)
- `render.yaml` — конфиг для Render
- `requirements.txt` — flask, gunicorn
- `AGENTS.md` — этот файл

## Данные

```json
{
  "credits": [
    {"id": "uuid", "name": "Ипотека", "monthly": 45000, "day": 15}
  ],
  "payments": {
    "creditId": {
      "2026-07": {"status": "paid|early", "date": "2026-07-15"}
    }
  }
}
```

## Статусы платежей

- `paid` — оплачено (зелёная ✓)
- `early` — оплачено досрочно (жёлтая ⚡)
- отсутствует — не оплачено (красная ●, если дата уже прошла)

## Логика календаря

- День платежа = `credit.day` число каждого месяца
- Под числом — иконка для каждого кредита
- Будущие дни кликабельны (можно оплатить досрочно)

## API

- `GET /api/data` — получить все кредиты и платежи
- `POST /api/data` — сохранить все данные (перезаписывает целиком)

## Деплой

- GitHub: `github.com/elkungurov/finance-manager`
- Render: авто-деплой из `main`
- Start command: `gunicorn server:app`
- Port: `$PORT` (5001 локально)

## Локальный запуск

```powershell
cd D:\finance-manager
python server.py
# http://localhost:5001
```
