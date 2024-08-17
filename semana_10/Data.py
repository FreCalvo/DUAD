# This module has de export and Import code only.

import csv

# Export data to CSV file.
def write_file(file_path, data, headers):
    with open(file_path, 'w', encoding= 'utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


# Import data from CSV file and print.
def import_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        reader = csv.DictReader(file)
        data = list(reader)
        return data
