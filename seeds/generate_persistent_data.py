import csv
from pathlib import Path
from pprint import pprint
from ..lib.credentials_sdk import Credentials_SDK
from ..lib.storage_crud import print_persistent_creds


CWD = Path(__file__).resolve().parent
DATA_START_FILE = Path(CWD, 'data_start.csv').resolve()

with open(DATA_START_FILE) as f:
    data = [line.rstrip() for line in f.readlines() if line.rstrip() != '']
    pprint(data)

c_sdk = Credentials_SDK()
data = csv.reader(data)

for user, pwd in data:
    c_sdk.store_creds(user, pwd)

print_persistent_creds()

