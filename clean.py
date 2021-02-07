import json
with open("config.json", "r") as c:
    config = json.load(c)
with open("ext_data.json", "r") as orig, open("cleaned_data.json", "w") as cln:
    data = json.load(orig)
    rating_mappings = [
        ("AS1", "ATC Applicant"),
        ("AS2", "ATC Trainee"),
        ("AS3", "Advanced ATC Trainee"),
        ("ADC", "Aerodrome Controller"),
        ("APC", "Approach Controller"),
        ("ACC", "Centre Controller"),
        ("SEC", "Senior Controller"),
        ("SAI","Senior ATC Instructor"),
        ("CAI", "Chief ATC Instructor")
    ]

    for row in data[config["region"]]:
        img_name = int(row["rating_num"])
        row["rating_num"] = [img_name, rating_mappings[img_name - 2][0], rating_mappings[img_name - 2][1]]

    json.dump(data, cln, indent=8)


