import datetime
from read_data import fromJson

def get_post_weekday(data: dict) -> dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    dict_ = {}
    for i in range(7):
        dict_[i] = 0
    for j in data["messages"]:
        if j["type"] == "message":
            date_6 = datetime.datetime.strptime(j["date"], "%Y-%m-%dT%H:%M:%S")
            dict_[date_6.weekday()] += 1
    return dict_

data = fromJson("data/result.json")
print(get_post_weekday(data))
# Output: {0: 178, 1: 8, 2: 214, 3: 9, 4: 232, 5: 9, 6: 6}