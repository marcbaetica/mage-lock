import csv
import sys
from pathlib import Path
from pprint import pprint

# TODO: Make PYTHONPATH or run as module at root dir for pythonic solution.
sys.path.append(str(Path(__file__).parent.parent))  # Workaround. 

from lib.constants import CREDS_DB_PATH, CREDS_SEEDS_FILE_PATH
from lib.credentials_sdk import Credentials_SDK
from lib.storage_crud import print_persistent_creds


def get_credentials_seeds_from_file():
    print('lala')
    print(CREDS_SEEDS_FILE_PATH)
    with open(CREDS_SEEDS_FILE_PATH) as f:
        # TODO: Remove identifier @[0].
        users_creds_seeds = [line.rstrip() for line in f.readlines() if line.rstrip() != '']
    return users_creds_seeds

def populate_storage_with_seeds(data, c_sdk):
    data = csv.reader(data)

    for user, pwd in data:
        c_sdk.store_creds(user, pwd)


'''
users_creds = get_credentials_seeds()
pprint(users_creds)
populate_storage_with_seeds(users_creds)
print_persistent_creds()
'''
c_sdk = Credentials_SDK()
print(c_sdk.get_creds())
credentials = get_credentials_seeds_from_file()
print(f'creds {credentials}')
populate_storage_with_seeds(credentials, c_sdk)

