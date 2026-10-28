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
| 1 | Creating a Basic HTML Template in Flask | — |
| 2 | Creating a Dynamic Template with Loops and Conditions in Flask | — |
| 3 | Displaying Data from JSON or CSV Files in Flask | — |
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

## Author

Thomas Corbel - [Corbel99](https://github.com/Corbel99)
