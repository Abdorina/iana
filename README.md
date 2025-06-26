# Health Management REST API

Этот сервер предоставляет API для управления медицинскими данными и интеграциями с сервисами здоровья.

## Функционал API

1. `GET /user/profile` - Получить профиль пользователя
2. `GET /health/metrics` - Получить медицинские показатели
3. `GET /recommendations?category={category}` - Получить рекомендации по категории
4. `POST /integrations` - Добавить новую интеграцию
5. `DELETE /integrations/{integration_id}` - Удалить интеграцию

## Требования

- Python 3.7+
- FastAPI
- Uvicorn

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/health-api.git
cd health-api



pip install -r requirements.txt