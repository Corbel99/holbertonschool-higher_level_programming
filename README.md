# Holberton School – Higher Level Programming

This repository gathers my projects from the **Higher Level Programming** track at [Holberton School](https://www.holbertonschool.com/).
Each folder is a standalone project focused on a specific Python topic: data serialization, databases and ORM, and building RESTful APIs.

## 🛠️ Technologies

- **Language:** Python 3
- **Data formats:** JSON, CSV, XML, Pickle
- **Databases:** MySQL, MySQLdb, SQLAlchemy
- **Web / API:** HTTP, Flask, authentication (Basic Auth & JWT)

## 📁 Projects

| Project | Description |
|---------|-------------|
| [python-serialization](./python-serialization) | Serialization and deserialization of Python data using JSON, Pickle, CSV and XML, along with file handling. |
| [python-object_relational_mapping](./python-object_relational_mapping) | Connecting Python to a MySQL database, first with raw SQL queries (MySQLdb), then through the SQLAlchemy ORM with mapped models (e.g. `State`, `City`). |
| [restful-api](./restful-api) | Building and consuming RESTful APIs in Python: HTTP requests, a simple API with Flask, and securing endpoints with Basic and JWT authentication. |

Each project folder contains its own `README.md` with the detailed learning objectives and tasks.

## 🎯 Learning Objectives

By completing these projects, I learned to:

- Convert Python objects to and from different data formats (JSON, CSV, XML, Pickle)
- Read and write files with Python's file handling mechanisms
- Interact with a relational database from a Python script
- Map database tables to Python classes using an ORM
- Understand how REST APIs and HTTP methods work
- Build an API with Flask and protect its routes with authentication

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/Corbel99/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming
```

Then move into a project folder and follow the instructions in its README:

```bash
cd python-serialization
```

### Requirements

- Python 3.8+
- MySQL server (for `python-object_relational_mapping`)
- Python packages, depending on the project:

```bash
pip install mysqlclient SQLAlchemy Flask Flask-HTTPAuth Flask-JWT-Extended requests
```

## 👤 Author

**Corbel99** – Full-stack developer student at Holberton School
GitHub: [@Corbel99](https://github.com/Corbel99)
