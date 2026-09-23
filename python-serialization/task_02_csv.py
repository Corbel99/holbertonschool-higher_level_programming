#!/usr/bin/env python3
"""Convert CSV data to JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON and save it to data.json."""
    try:
        with open(csv_filename, mode="r") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", mode="w") as file:
            json.dump(data, file)

        return True

    except FileNotFoundError:
        return False
