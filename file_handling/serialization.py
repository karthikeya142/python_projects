#Serialization in Python is the process of converting an object into a format
# that can be easily stored or transmitted and then reconstructed later.
# This is useful for saving data to a file, sending it over a network, or storing it in a database.
import json
import pickle

# Python object (dictionary)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialization: Python object to JSON string
json_string = json.dumps(data)
print(f'serialization  {json_string}')  # Output: {"name": "John", "age": 30, "city": "New York"}
json_string1 = json.loads(json_string)
print(type(f'serialization (type {json_string1})') ) # Output: {"name": "John", "age": 30, "city": "New York"}

# Deserialization: JSON string to Python object
data_back = json.loads(json_string)
print(f' Deserialization {data_back}')  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
# Serialize to pickle

pickle_data = pickle.dumps(data)
print(f'  {pickle_data}')

# Deserialize from pickle
data_back = pickle.loads(pickle_data)
print(f'  {pickle_data}')


#Deserialization in Python is the process of converting a serialized data format(such as JSON,XML,or binary data)back into a Python object.
# Serialization is the process of converting a Python object into a serialized format. Together,
# they allow for the storage or transmission of Python objects in a format that can be easily reconstructed later.