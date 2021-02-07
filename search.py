import json

# Search for all TWR position with AS2 requirement
with open("cleaned_data.json", "r") as f, open("config.json") as c:
    config = json.load(c)
    data = json.load(f)
    for row in data[config["region"]]:
        if "TWR" in row["airport"].upper() and row["rating_num"][0] == 3:
            print(row)
