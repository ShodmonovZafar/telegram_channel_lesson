import json
from read_data import fromJson

def get_post_per_week(data: dict, month: int) -> dict:
    map_ = {}
    for j in range(1, 6):
        map_[j] = 0
        
    for i in data["messages"]:
        
        if i["type"] == "message" and int(i["date"][5:7]) == month:
            week_ = int(i["date"][8:10])
            if 1 <= week_ <= 7:
                map_[1] += 1
            elif 7 < week_ <= 14:
                map_[2] += 1
            elif 14 < week_ <= 21:
                map_[3] += 1
            elif 21 < week_ <= 28:
                map_[4] += 1
            else:
                map_[5] += 1
    return map_

path_to_the_json_document = "data/result.json"

with open(path_to_the_json_document, "r", encoding='utf8') as f:
    data = json.load(f)

natija = get_post_per_week(data, 10)
print(natija)