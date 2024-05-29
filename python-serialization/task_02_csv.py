#!/usr/bin/env python3
import csv
import json

"""
Function to convert a CSV to JSON
Args: csvFilePath, jsonFilePath
"""
csv_file = 'input.csv'
json_file = 'output.json'

def convert_csv_to_json(csv_file, json_file):
    """
    Create a dictionary
    """
    data = []

    """
    Open a csv reader
    """
    with open(csvFilePath, 'r') as csvf:
        csvReader = csv.DictReader(csvf)
        """
        Convert each row into a dictionary
        add it to data
        """
        for row in csvReader:

            """
            Primary key
            """
            data.append(row)

    """
    Open a json writer and use the json.dumps()
    function to dump data
    """
    with open(jsonFilePath, 'w') as jsonf:
        json.dump(data, jsonFile)
    """
    Decide the two file paths according to your
    computer system
    """
    csvFilePath = r'Names.csv'
    jsonFilePath = r'Names.json'

    """
    Call the convert_csv_to_json
    """
    convert_csv_to_json(csvFilePath, jsonFilePath)
