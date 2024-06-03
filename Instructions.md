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

pip install -r services/requirements.txt 
```
Запустить сервис 

```
cd ml_service
uvicorn main:app
```


### 2. FastAPI микросервис в Docker-контейнере
...


### 3. Запуск сервисов для системы мониторинга

### 4. Построение дашборда для мониторинга