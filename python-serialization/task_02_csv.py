#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_file, json_file):

    try:
        with open(csvFilePath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
