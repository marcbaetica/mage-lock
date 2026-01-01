import json
from pprint import pprint
from .constants import CREDS_DB_PATH


class CredentialsSDK:
    def get_creds(self) -> dict:
        print(f'Attempting to extract credentials from db [{CREDS_DB_PATH}].')
        if not CREDS_DB_PATH.exists():
            print(f'Persistence storage does not currently exist under [{CREDS_DB_PATH}].')
            return dict()
        with open(CREDS_DB_PATH, 'r') as f:
            creds = json.loads(f.readline().rstrip())
            print(f'Retrieved credentials from db:')
            pprint(creds)
            return creds

    def store_creds(self, new_credentials: dict):
        print(f'Attempting to add credentials [{new_credentials}] to db [{CREDS_DB_PATH}].')
        curr_creds = self.get_creds()
        curr_creds.update(new_credentials)
        with open(CREDS_DB_PATH, 'w') as f:
            f.write(json.dumps(curr_creds))
        print(f'Done. Checking if the new data was added.')
        self.get_creds()

    def flush_creds(self):
        print(f'Attempting to flush db under [{CREDS_DB_PATH}].')
        CREDS_DB_PATH.unlink(missing_ok=True)
        print(f'DB was flushed: [{not CREDS_DB_PATH.exists()}]')

