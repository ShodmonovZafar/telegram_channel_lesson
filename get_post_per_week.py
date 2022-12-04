import json
import datetime
from read_data import fromJson

def get_post_per_week(data: dict, month: int) -> dict:
    map_ = {}
    for j in range(1, 6):
        map_[j] = 0
        
    for i in data["messages"]:
        date_ = datetime.datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S")
        if i["type"] == "message" and date_.month == month:
            day_ = date_.day
            if 1 <= day_ <= 7:
                map_[1] += 1
            elif 7 < day_ <= 14:
                map_[2] += 1
            elif 14 < day_ <= 21:
                map_[3] += 1
            elif 21 < day_ <= 28:
                map_[4] += 1
            else:
                map_[5] += 1
    return map_

path_to_the_json_document = "data/result.json"

with open(path_to_the_json_document, "r", encoding='utf8') as f:
    data = json.load(f)

natija = get_post_per_week(data, 10)
# {1: 68, 2: 77, 3: 76, 4: 93, 5: 20}
print(natija)