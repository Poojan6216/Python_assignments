def parse_string(string1):
    parts = string1.split("0")
    filtered_parts = [part for part in parts if part]

    return{
        "first_name": filtered_parts[0],
        "last_name": filtered_parts[1],
        "id": filtered_parts[2]
    }

string1 = "Robert000000Smith000123"
result = parse_string(string1)
print(result)