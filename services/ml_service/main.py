# импортируем класс для создания экземпляра FastAPI приложения
from fastapi import FastAPI, Body
from ml_service.fast_api_handler import FastApiHandler

# создаём экземпляр FastAPI приложения
app = FastAPI()
app.handler=FastApiHandler()

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World"}


# обрабатываем запросы к специальному пути для получения предсказания модели

@app.post("/api/get_prediction/")
def get_prediction_for_item(
    model_features: dict = Body(
        default={
            "flat_id":10769,
            "floor":9,
            "is_apartment": "false",
            "kitchen_area": 8.946669, 
            "living_area":33.0,
            "rooms":2, 
            "total_area":43.900002, 
            "building_id":4431, 
            "build_year":1962, 
            "building_type_int":4,
            "latitude":55.705067,
            "longitude":37.763611,
            "ceiling_height": 2.64,
            "flats_count":72,
            "floors_total":9, 
            "has_elevator": "true"
        }
    )
):
    all_params = {
        "model_features": model_features
    }
    return app.handler.handle(all_params)
