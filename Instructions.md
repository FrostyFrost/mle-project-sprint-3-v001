# Инструкции по запуску микросервиса

### 1. FastAPI микросервис в виртуальном окружение
Клонирование проекта и установка окружения

```
git clone git@github.com:FrostyFrost/mle-project-sprint-3-v001.git
cd mle-project-sprint-3-v001

sudo apt-get update
sudo apt-get install python3.10-venv
python3.10 -m venv .venv_sprint03
source .venv_sprint03/bin/activate

cd services
pip install -r requirements.txt 
```
Запустить сервис 

```
uvicorn ml_service.main:app
```

Сервис принимает запросы на endpoint /api/get_prediction/

Пример запроса:
```
curl -X 'POST' \
  'http://localhost:8080/api/get_prediction/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "flat_id": 10769,
  "floor": 9,
  "is_apartment": "false",
  "kitchen_area": 8.946669,
  "living_area": 33,
  "rooms": 2,
  "total_area": 43.900002,
  "building_id": 4431,
  "build_year": 1962,
  "building_type_int": 4,
  "latitude": 55.705067,
  "longitude": 37.763611,
  "ceiling_height": 2.64,
  "flats_count": 72,
  "floors_total": 9,
  "has_elevator": "true"
}'
```

### 2. FastAPI микросервис в Docker-контейнере
#### Docker
Инструкции Docker содержатся в файле ```Dockerfile_ml_service``` 

Собрать образ 
```
docker image build . -f Dockerfile_ml_service --tag estate_predict_service:0
```

Запускать сервис командой 
```
docker container run --publish 8080:8080 --env-file=.env estate_predict_service:0 
```

Остановить:
```
docker container ps
```
Найти нужный hash
```
docker stop <hash>
```

#### Docker compose
Запуск командой 
```
docker compose up --build
```

`commit: port from env`
### 3. Запуск сервисов для системы мониторинга
Порты:
* ml_service: 8080 
* prometheus: 9090
* grafana: 3000

Запуск командой 
```
docker compose up --build
```

### 4. Построение дашборда для мониторинга
Скрипт для проверки загрузки сервера. Отрабатывает примерно в течение 2 минут.
```
 python3 test_requests.py 
```