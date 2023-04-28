# Burrowkv

Burrowkv is a simple key-value store implementation in Python. It provides basic functionality to store and retrieve key-value pairs, as well as additional features such as JSON serialization and deserialization.

## Features

- Set a value for a given key.
- Retrieve the value associated with a key.
- Delete a key-value pair.
- Check if a key exists in the store.
- Get a list of all keys.
- Get a list of all values.
- Get a list of all key-value pairs.
- Serialize the key-value store to JSON.
- Deserialize JSON into the key-value store.

## Installation

```
pip install burrowkv
```

## Usage
```
from burrowkv import burrowkv

# Create a new instance of burrowkv
store = burrowkv()

# Set a value for a key
store.set('name', 'John')

# Retrieve the value associated with a key
name = store.get('name')  # Returns 'John'

# Delete a key-value pair
store.delete('name')

# Check if a key exists
if store.contains('name'):
    print('Key exists')
else:
    print('Key does not exist')

# Get a list of all keys
keys = store.keys()  # Returns a list of keys

# Get a list of all values
values = store.values()  # Returns a list of values

# Get a list of all key-value pairs
items = store.items()  # Returns a list of (key, value) tuples

# Serialize the key-value store to JSON

json_data = store.to_json()

# Deserialize JSON into the key-value store
store.from_json(json_data)
```

## License
This project is licensed under the MIT License. See the LICENSE file for more information.