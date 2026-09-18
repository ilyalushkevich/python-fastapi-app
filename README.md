# Books API

REST API для управления коллекцией книг, построенный на FastAPI.

## Технологии

- **Python 3.13**
- **FastAPI 0.141** — веб-фреймворк
- **Pydantic v2** — валидация данных
- **Uvicorn** — ASGI-сервер
- **pytest + allure-pytest** — тестирование и отчёты
- **ruff + flake8** — линтеры

## Быстрый старт

### Локально

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

API будет доступно на `http://localhost:8000`.  
Интерактивная документация: `http://localhost:8000/docs`.

### Docker

```bash
docker build -t books-api .
docker run -p 8000:8000 books-api
```

## API

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/` | Статус сервиса |
| `POST` | `/books/` | Создать книгу |
| `GET` | `/books/` | Список всех книг |
| `GET` | `/books/{id}` | Получить книгу по ID |
| `PUT` | `/books/{id}` | Обновить книгу |
| `DELETE` | `/books/{id}` | Удалить книгу |

### Примеры запросов

**Создать книгу**
```bash
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Clean Code", "author": "Robert Martin", "description": "A handbook of agile software craftsmanship"}'
```

**Получить все книги**
```bash
curl http://localhost:8000/books/
```

**Обновить книгу**
```bash
curl -X PUT http://localhost:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Clean Code (2nd Edition)"}'
```

**Удалить книгу**
```bash
curl -X DELETE http://localhost:8000/books/1
```

## Тесты

**Запустить все тесты:**
```bash
pytest
```

**С отчётом о покрытии:**
```bash
pytest --cov=src
```

**С генерацией Allure-отчёта:**
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Структура проекта

```
.
├── src/
│   ├── main.py          # Точка входа, инициализация приложения
│   ├── models.py        # Модель данных и in-memory хранилище
│   ├── schemas.py       # Схемы запросов и ответов
│   ├── crud.py          # Операции с данными
│   └── routers/
│       └── books.py     # Роуты /books
├── tests/
│   ├── unit/            # Unit-тесты
│   └── allure/          # Тесты с Allure-шагами
├── ci/
│   └── allure/
│       ├── Dockerfile              # Nginx-образ для публикации Allure-отчёта
│       └── Dockerfile.dockerignore # dockerignore для этой сборки (не даёт корневому .dockerignore исключить allure-report/)
├── Dockerfile
├── pyproject.toml       # Конфиг pytest (testpaths, filterwarnings)
├── requirements.txt
├── .dockerignore
└── .gitignore
```
