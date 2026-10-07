# RESTful API

## Description

This project introduces the fundamentals of RESTful APIs and HTTP communication using Python.

The exercises cover how to interact with APIs from the command line, consume API data with Python, create APIs, handle authentication and document APIs using OpenAPI standards.

## Learning Objectives

At the end of this project, I should be able to:

- Understand the fundamentals of HTTP and HTTPS.
- Use `curl` to interact with APIs from the command line.
- Consume API data using Python and the `requests` library.
- Parse and manipulate JSON data.
- Convert structured API data into CSV format.
- Build a simple API using Python.
- Build APIs using Flask.
- Understand API authentication and security.
- Understand and use OpenAPI documentation.

## Tasks

### Task 0 — Basics of HTTP/HTTPS

Introduction to HTTP and HTTPS, including:

- HTTP requests and responses.
- HTTP methods.
- HTTP status codes.
- Headers and body.
- Differences between HTTP and HTTPS.

### Task 1 — Consume data from an API using `curl`

Using `curl` to:

- Make HTTP requests from the command line.
- Retrieve data from an API.
- Inspect HTTP headers.
- Send POST requests.
- Interpret API responses.

The exercises use **JSONPlaceholder** as a public API for testing.

### Task 2 — Consume and process data from an API using Python

Using Python and the `requests` library to:

- Send HTTP GET requests.
- Check HTTP status codes.
- Parse JSON responses.
- Extract information from API data.
- Convert API data into a list of dictionaries.
- Export the data to a CSV file.

The main Python file for this task is:

```text
task_02_requests.py
```

The generated CSV file is:

```text
posts.csv
```

## Technologies

- Python 3.9
- HTTP / HTTPS
- REST APIs
- `curl`
- Python `requests`
- JSON
- CSV
- Flask
- OpenAPI

## Repository

**GitHub repository:** `holbertonschool-higher_level_programming`

**Project directory:** `restful-api`