# импортируем библиотеку для работы со случайными числами
import random

# импортируем класс для создания экземпляра FastAPI приложения
from fastapi import FastAPI
from fast_api_handler import FastApiHandler

# создаём экземпляр FastAPI приложения
app = FastAPI()
app.handler=FastApiHandler()

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World"}


# обрабатываем запросы к специальному пути для получения предсказания модели
# предсказание пока что в виде заглушки со случайной генерацией score
@app.post("/api/get_prediction/{flat_id}")
def get_prediction_for_item(flat_id: str, model_features: dict):
    all_params = {
        "flat_id": flat_id,
        "model_features": model_features
    }
    return app.handler.handle(all_params)
   # return {"user_id": flat_id, "score": model_features}
