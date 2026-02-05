# Chat-api
Chat API

REST API для чатов и сообщений на FastAPI + PostgreSQL
с миграциями Alembic, логированием и тестами pytest.

Стек технологий:
-Python 3.11
-FastAPI
-SQLAlchemy
-PostgreSQL 15
-Alembic
-Docker & Docker Compose
-Pytest
-Pydantic v2

Функциональность:
-Создание чатов
-Отправка сообщений в чат
-Получение чата с последними N сообщениями
-Удаление чата с каскадным удалением сообщений
-Валидация входных данных
-Логирование запросов
-Автоматическое применение миграций
-Тесты API

Запуск проекта (одной командой):
docker compose up --build

http://localhost:8000/docs

Запуск тестов:
docker compose exec api pytest -v

Создание новой миграции:
docker compose exec api alembic revision --autogenerate -m "message"

Применение миграций:
docker compose exec api alembic upgrade head

Логи выводятся в stdout контейнера:
docker compose logs api