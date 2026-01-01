import csv
from pathlib import Path
from pprint import pprint


curr_dir = Path(__file__).parent
csv_file_path = Path(curr_dir, 'data_start.csv')
print(csv_file_path)

def get_credentials_seeds():
    with open(csv_file_path, 'r') as csv_file:
        data_to_store = dict()
        rows = csv.DictReader(csv_file)
        for row in rows:
            data_to_store.update({row['user']: row['pass']})
        return data_to_store

