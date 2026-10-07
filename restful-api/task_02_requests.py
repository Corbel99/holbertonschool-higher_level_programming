#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    data = response.json()

    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    data = response.json()

    post_list = []

    for post in data:
        new_post = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        post_list.append(new_post)

    with open("posts.csv", "w") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(post_list)
