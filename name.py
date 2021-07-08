import json

# example dictionary to save as JSON
"""
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@doe.com",
    "salary": 1499.9, # just to demonstrate we can use floats as well
    "age": 17,
    "is_real": False, # also booleans!
    "titles": ["The Unknown", "Anonymous"] # also lists!
}

# save JSON file
# 1st option
with open("data1.json", "w") as f:
    json.dump(data, f)
""" 
file_name = "data1.json"
with open(file_name) as f:
    data = json.load(f)
    
print(data)