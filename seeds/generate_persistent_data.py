import csv
from pathlib import Path
from pprint import pprint


CWD = Path(__file__).resolve().parent
DATA_START_FILE = Path(CWD, 'data_start.csv').resolve()

with open(DATA_START_FILE) as f:
    data = [line.rstrip() for line in f.readlines() if line.rstrip() != '']
    pprint(data)

data = csv.reader(data)
# print(data)
# pprint(list(data))

while True:
    try:
        item = next(data)
        print(type(item), item)
    except StopIteration:
        break

