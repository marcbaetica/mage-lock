import csv
import sys
from pathlib import Path
from pprint import pprint

# TODO: Make PYTHONPATH or run as module at root dir for pythonic solution.
sys.path.append(str(Path(__file__).parent.parent))  # Workaround. 

from lib.constants import CREDS_DB_PATH, CREDS_SEEDS_FILE_PATH
from lib.credentials_sdk import CredentialsSDK


def get_credentials_seeds_from_file():
    print(f'Extracting credentials from [{CREDS_SEEDS_FILE_PATH}].')
    with open(CREDS_SEEDS_FILE_PATH, 'r') as csv_file:
        credentials_seeds = dict()
        rows = csv.DictReader(csv_file)
        for row in rows:
            credentials_seeds.update({row['user']: row['pass']})
        return credentials_seeds


def populate_storage_with_seeds(credentials_seeds: dict, c_sdk: CredentialsSDK):
    c_sdk.store_creds(credentials_seeds)



c_sdk = CredentialsSDK()
credentials_seeds = get_credentials_seeds_from_file()
print(f'Retrieved seed data:')
pprint(credentials_seeds)
populate_storage_with_seeds(credentials_seeds, c_sdk)
c_sdk.flush_creds()

