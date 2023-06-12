# Название
quiz_app

## Описание
Web-сервис для игры в викторину.
## Использованные технологии
- Docker
- Fastapi
- SQLAlchemy
- requests
- uvicorn

# Установить все необходимые зависимости
$ pip install -r requirements.txt

# Запустить Docker контейнеры
$ docker-compose up -d

# Запустить сервер 
$ docker-compose up --build

# Для отправки запроса на создание вопроса необходимо (на Линукс)
$ curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 10}' http://example.com/questions/
 
# Для отправки запроса на создание вопроса на Windows необходимо установить curl https://curl.se/windows/ затем ввести команду
$ path_to_curl.exe" -X POST -H "Content-Type: application/json" -d "{\"questions_num\": 10}" http://example.com/questions/

