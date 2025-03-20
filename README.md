![Image alt](https://github.com/MorozGH/education_project/blob/main/erd.jpg)

# Translation Service API

FastAPI-бэкенд для сервиса переводов с системой аутентификации, управлением заказами и балансом.

## 📌 Основные возможности

- ✅ Регистрация и аутентификация пользователей
- 🔐 JWT-токены для доступа к API
- 💰 Управление балансом пользователя
- 📦 Создание/управление заказами на перевод
- 📊 История транзакций
- 🔄 RESTful API с документацией Swagger/Redoc

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.7+
- PIP

### 🛠 Технологии

FastAPI - Веб-фреймворк

SQLAlchemy - ORM

Pydantic - Валидация данных

JWT - Аутентификация

SQLite - База данных

Python-dotenv - Управление окружением

### Установка
```bash
git clone https://github.com/MorozGH/education_project.git
cd education_project
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
