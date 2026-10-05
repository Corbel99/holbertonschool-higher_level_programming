# Python - Object-Relational Mapping

## Description

This project introduces the connection between Python and relational databases.

The first part of the project focuses on using the `MySQLdb` module to connect to a MySQL database and execute SQL queries from Python.

The second part introduces SQLAlchemy and Object-Relational Mapping (ORM), allowing Python classes and objects to interact with database tables.

## Learning Objectives

At the end of this project, you should be able to:

- Connect to a MySQL database from a Python script
- Select rows from a MySQL table using Python
- Insert rows into a MySQL table using Python
- Explain what an ORM is
- Map a Python class to a MySQL table

## Requirements

- Python 3
- MySQL
- MySQLdb (`mysqlclient`)
- SQLAlchemy
- Pycodestyle 2.7.*

All Python files:

- Must start with `#!/usr/bin/python3`
- Must end with a new line
- Must be executable
- Must contain module documentation
- Must contain documentation for classes and functions
- Must follow the pycodestyle style guide

## Task 0 - Get all states

The first task uses `MySQLdb` to connect to the MySQL database and retrieve all rows from the `states` table.

The results are sorted by `states.id` in ascending order.

Example:

```bash
./0-select_states.py root root hbtn_0e_0_usa