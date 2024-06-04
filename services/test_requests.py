import requests
import time
import random

for i in range(20):
    params = {
        "flat_id":i,
        "floor":random.randrange(0, 101),
        "is_apartment": "false",
        "kitchen_area": random.uniform(10, 150), 
        "living_area":random.uniform(10, 150),
        "rooms":random.randrange(0, 5), 
        "total_area":random.uniform(10, 150), 
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
    response = requests.post('http://localhost:8080/api/get_prediction/', json=params)

time.sleep(10)
for i in range(20):
    params = {
        "flat_id":20+i,
        "floor":random.randrange(0, 101),
        "is_apartment": "false",
        "kitchen_area":random.uniform(10, 150), 
        "living_area":random.uniform(10, 150),
        "rooms":random.randrange(0, 5), 
        "total_area":random.uniform(20, 250), 
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
    response = requests.post('http://localhost:8080/api/get_prediction/', json=params)
    time.sleep(3)
