import datetime
from read_data import fromJson

def get_post_per_month(data: dict) -> dict:
    map_ = {}
    
    # Set months to 0
    for i in range(1, 32):
        map_[i] = 0
        
    for e in data["messages"]:
        type_ = e["type"]
        date_ = datetime.datetime.strptime(e["date"], "%Y-%m-%dT%H:%M:%S")
        day_ = date_.day
        if type_ == "message":
            map_[day_] += 1
    return map_


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)
"""
# Output: {1: 8, 2: 45, 3: 22, 4: 27, 5: 11, 6: 2, 7: 61, 8: 1, 9: 24, 10: 19, 11: 13, 12: 24, 13: 2, 14: 52, 15: 0, 16: 37, 17: 24, 18: 35, 19: 9, 20:
1, 21: 56, 22: 0, 23: 22, 24: 9, 25: 11, 26: 48, 27: 0, 28: 43, 29: 0, 30: 30, 31: 20}
"""