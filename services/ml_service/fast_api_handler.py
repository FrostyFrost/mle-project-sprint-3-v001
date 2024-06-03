# coding: utf-8
"""Класс FastApiHandler, который обрабатывает запросы API."""
import pickle
import pandas as pd


class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # Типы параметров запроса для проверки
        self.param_types = {
            "model_features": dict
        }
        
        self.pipeline_path = "../models/pipeline_zero.pkl"
        self.load_pipeline(pipeline_path=self.pipeline_path)
        
        # Необходимые параметры для предсказаний модели оттока
        self.required_model_features = [
            "flat_id",
            "floor",
            "is_apartment",
            "kitchen_area", 
            "living_area",
            "rooms", 
            "total_area", 
            "building_id", 
            "build_year", 
            "building_type_int",
            "latitude",
            "longitude",
            "ceiling_height",
            "flats_count",
            "floors_total", 
            "has_elevator"
        ]

    def load_pipeline(self, pipeline_path: str):
        """Загружаем обученную модель предсказания цены.
        Args:
            pipeline_path (str): Путь до модели.
        """
        try:
            with open(pipeline_path, "rb") as f:
                self.pipeline = pickle.load(f)

        except Exception as e:
            print(f"Failed to load model: {e}")

    def model_predict(self, model_features: dict) -> float:
        """Предсказываем цену.

        Args:
            model_features (dict): Параметры для модели.

        Returns:
            float - цена квартиры
        """
        param_values_list = pd.DataFrame.from_dict(model_features, orient='index').T
        return self.pipeline.predict(param_values_list)[0]
        
    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора параметров.
        
        Args:
            query_params (dict): Параметры запроса.
        
        Returns:
                bool: True - если есть нужные параметры, False - иначе
        """
        if "model_features" not in query_params:
            return False
        
        if not isinstance(query_params["model_features"], self.param_types["model_features"]):
            return False
        return True
    
    def check_required_model_features(self, model_features: dict) -> bool:
        """Проверяем фичи на наличие обязательного набора.
    
        Args:
            model_features (dict): Фичи объекта для предсказания
    
        Returns:
            bool: True - если есть нужные параметры, False - иначе
        """
        if set(model_features.keys()) == set(self.required_model_features):
            return True
        return False
    
    def validate_params(self, params: dict) -> bool:
        """Разбираем запрос и проверяем его корректность.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Cловарь со всеми параметрами запроса.
        """
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_features(params["model_features"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
		
    def handle(self, params):
        """Функция для обработки запросов API параметров входящего запроса.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Словарь, содержащий результат выполнения запроса.
        """
        try:
            # Валидируем запрос к API
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                
                model_features = params["model_features"]
                print(f"Predicting for flat:\n{model_features}")
                # Получаем предсказания модели
                
                #print(list(model_features.values()))
                
                score = self.model_predict(model_features)
                response = {
                    "flat_id": model_features['flat_id'], 
                    "score": score
                }
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response

if __name__ == "__main__":

    # Создаем тестовый запрос
    test_params = {
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

    # Создаем обработчик запросов для API
    handler = FastApiHandler()

    # Делаем тестовый запрос
    response = handler.handle(test_params)
    