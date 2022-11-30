from read_data import fromJson

def get_post_per_month(data: dict) -> dict:
    map_ = {}
    
    # Set months to 0
    for i in range(1, 13):
        map_[i] = 0
        
    for e in data["messages"]:
        type_ = e["type"]
        month_ = int(e["date"][5:7])
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