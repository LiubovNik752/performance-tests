import json


json_data = '{"name": "Ivan", "age": 20, "city": "New York"}'

parsed_data = json.loads(json_data)
print(parsed_data)

data = {
    "name": "Ivan",
    "age": 20,
    "is_student": True,
    "city": "New York"
}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", encoding="utf-8") as file:
    data = json.load(file)
    print(data)