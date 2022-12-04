import datetime
from read_data import fromJson

def get_post_per_month(data: dict) -> dict:
    map_ = {}
    
    # Set months to 0
    for i in range(1, 13):
        map_[i] = 0
        
    for e in data["messages"]:
        type_ = e["type"]
        date_ = datetime.datetime.strptime(e["date"], "%Y-%m-%dT%H:%M:%S")
        month_ = date_.month
        if type_ == "message":
            map_[month_] += 1
    return map_


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)
# Output: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 30, 10: 334, 11: 292, 12: 0}