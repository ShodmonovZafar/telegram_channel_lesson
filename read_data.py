import json

def fromJson(file_path: str) -> dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    # open file
    with open(file_path, "r", encoding="utf8") as f:
        # f = open(file_path, "r", encoding='utf8').read()
        # load json
        data = json.load(f)
    return data


# print(fromJson("data/result.json"))