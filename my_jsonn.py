import json
json_data = '{"name": "Alice", "age": 30, "city":"New York"}'
person = json.loads(json_data)
print(person["name"])  
print(person["age"])   