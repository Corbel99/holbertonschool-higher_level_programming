#!/usr/bin/env python3

import pickle


class CustomObject:
    """Represent a custom Python object that can be serialized."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return it."""
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
