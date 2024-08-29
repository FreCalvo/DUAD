# This module has de export and Import code only.

import csv
import os
from collections import defaultdict
from OOP_Actions import Student
from typing import List


# Export data to CSV file.
def objects_to_dicts(objects):
    dicts = []
    for obj in objects:
        obj_dict = defaultdict(lambda: None)
        for key, value in vars(obj).items():
            obj_dict[key] = value
        dicts.append(dict(obj_dict))
    return dicts


def write_dicts_to_csv(dicts, file_path):
    """Writes a list of dictionaries to a CSV file.

    Args:
        dicts (list): The list of dictionaries to write.
        file_path (str): The path to the CSV file.
    """

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = dicts[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dicts)


# Import data from CSV file and print.
def read_csv_to_objects(file_path: str) -> List[Student]:
    """Reads a CSV file and converts its content into a list of Student objects.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[Student]: A list of Student objects.
    """

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            students = [Student(**row) for row in reader]
            return students
    else:
        return []

