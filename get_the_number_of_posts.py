
def get_the_number_of_posts(data: dict) -> int:
    count = 0
    for e in data["messages"]:
        if e["type"] == "message":
            count += 1
    return count
