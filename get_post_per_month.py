from read_data import fromJson
from get_post_month import get_post_month
def get_post_per_month(data:dict)->dict:
    map_ = {}
    for i in range(1, 13):
        p = get_post_month(data, i)
        map_[i] = p
    
  
    
    return map_


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)