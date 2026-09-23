# Python - Serialization

This project introduces serialization and deserialization in Python using different data formats and techniques.

## Learning Objectives

At the end of this project, you should be able to:

- Understand the concept of serialization and deserialization.
- Serialize and deserialize Python data using JSON.
- Serialize and deserialize custom Python objects using Pickle.
- Convert CSV data into JSON format.
- Serialize and deserialize Python dictionaries using XML.
- Work with files using Python's file handling mechanisms.

## Tasks

### 0. Basic Serialization

Learn how to serialize and deserialize Python data using the `json` module.

- Serialize Python data into a JSON file.
- Load JSON data back into Python.

### 1. Pickling Custom Classes

Learn how to serialize custom Python objects using the `pickle` module.

The task implements a `CustomObject` class with:

- `name`
- `age`
- `is_student`

The object can be serialized to a binary file and later deserialized into a new instance.

### 2. Converting CSV Data to JSON

Convert data from a CSV file into JSON format.

The task uses:

- `csv.DictReader` to read CSV data.
- `json.dump` to serialize the data.
- File handling to create the resulting `data.json` file.

### 3. Serializing and Deserializing with XML

Explore XML as an alternative serialization format.

The task uses Python's `xml.etree.ElementTree` module to:

- Create an XML tree from a Python dictionary.
- Save the XML data to a file.
- Read an XML file.
- Reconstruct the original Python dictionary.

## Technologies

- Python 3
- JSON
- Pickle
- CSV
- XML
- `xml.etree.ElementTree`

## Requirements

- Ubuntu 20.04 LTS
- Python 3
- PEP 8 compliant code
- All files should be executable where required.

## Repository

**GitHub repository:** `holbertonschool-higher_level_programming`

**Directory:** `python-serialization`
