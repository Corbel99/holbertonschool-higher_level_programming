# Python - Server-Side Rendering

This project is part of the Holberton School curriculum (`holbertonschool-higher_level_programming`).

## Description

Server-side rendering (SSR) is a technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering (CSR), where the browser builds the page using JavaScript and dynamic data.

In this project, SSR is implemented in Python with the Flask framework and the Jinja templating engine, using data from JSON, CSV and SQLite sources.

## Learning Objectives

- Understand server-side rendering and how it differs from client-side rendering
- Know the benefits of server-side rendering in web development
- Implement SSR in Python using Flask
- Use the Jinja templating engine to generate dynamic HTML pages
- Read and display data from JSON, CSV and SQLite sources
- Handle dynamic content and user inputs in web applications

## Requirements

- Python 3
- Flask (`pip install Flask`)

## Tasks

| # | Task | File(s) |
|---|------|---------|
| 0 | Creating a Simple Templating Program | `task_00_intro.py` |
| 1 | Creating a Basic HTML Template in Flask | `task_01_jinja.py`, `templates/index.html`, `templates/about.html`, `templates/contact.html`, `templates/header.html`, `templates/footer.html` |
| 2 | Creating a Dynamic Template with Loops and Conditions in Flask | `task_02_logic.py`, `templates/items.html`, `items.json` |
| 3 | Displaying Data from JSON or CSV Files in Flask | `task_03_files.py`, `templates/product_display.html`, `products.json`, `products.csv` |
| 4 | Extending Dynamic Data Display to Include SQLite in Flask | — |

### 0. Creating a Simple Templating Program

A function `generate_invitations(template, attendees)` that generates personalized invitation files (`output_1.txt`, `output_2.txt`, ...) from a template with placeholders (`{name}`, `{event_title}`, `{event_date}`, `{event_location}`) and a list of dictionaries.

- Invalid input types: logs an error and stops
- Empty template: logs `Template is empty, no output files generated.`
- Empty list: logs `No data provided, no output files generated.`
- Missing values are replaced with `N/A`

Usage:

```
$ python3 main_0.py
```

### 1. Creating a Basic HTML Template in Flask

A basic Flask application that serves three pages (`/`, `/about`, `/contact`) rendered with Jinja templates. A reusable header (with navigation links) and footer are shared by every page using `{% include %}`.

Usage:

```
$ python3 task_01_jinja.py
```

Then open `http://127.0.0.1:5000/` in a browser.

### 2. Creating a Dynamic Template with Loops and Conditions in Flask

A `/items` route that reads a list of items from `items.json` and passes it to the `items.html` template. The template uses a Jinja `{% for %}` loop to display the items as an unordered list, and an `{% if %}` condition to display `No items found` when the list is empty.

Usage:

```
$ python3 task_02_logic.py
```

Then open `http://127.0.0.1:5000/items` in a browser.

### 3. Displaying Data from JSON or CSV Files in Flask

A `/products` route that reads product data from `products.json` or `products.csv`, depending on the `source` query parameter, and displays it in a table (Name, Category, Price). An optional `id` parameter filters a single product.

- Invalid source: displays `Wrong source`
- Unknown `id`: displays `Product not found`

Usage:

```
$ python3 task_03_files.py
```

Then open for example:

- `http://127.0.0.1:5000/products?source=json`
- `http://127.0.0.1:5000/products?source=csv&id=1`

## Author

Thomas Corbel - [Corbel99](https://github.com/Corbel99)
