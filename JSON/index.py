import json

person = '{"name": "John", "age": 30, "city": "New York"}'

result = json.loads(person) 
print(result) 