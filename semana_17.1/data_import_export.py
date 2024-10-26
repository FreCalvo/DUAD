import csv
import os


def export_data(data_array, file_name):
    """
    Exports data_array to a CSV file with the given filename.
    """
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(headings)  # Write headers first
        writer.writerows(data_array)

def import_data(file_name, data_array):
    if os.path.exists(file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # header = next(reader)  # Skip header row if present
            for row in reader:
                data_array.append(row)
    else:
        return []