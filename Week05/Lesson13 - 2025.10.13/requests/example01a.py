import json

# To convert a JSON string into a Python dictionary, you can use the JSON module, Here's an example:
json_string = '{"name": "John", "age": 25, "city": "New York"}'

python_dict = json.loads(json_string)
print(python_dict["name"])  # John


# To convert a Python dictionary to a JSON string, you can use the JSON module, Here's an example
python_dict = {"name": "John", "age": 40}
json_string = json.dumps(python_dict, ensure_ascii=False)
print(json_string)  # {"name": "John", "age": 40}
