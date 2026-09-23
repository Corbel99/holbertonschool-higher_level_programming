#!/usr/bin/env python3


import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, mode="w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load a JSON file and deserialize it into a Python dictionary."""
    with open(filename, mode="r") as file:
        return json.load(file)
