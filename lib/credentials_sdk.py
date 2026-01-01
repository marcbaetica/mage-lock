import json
from .constants import CREDS_DB_PATH


class Credentials_SDK:
    def get_creds(self) -> dict:
        print(f'Attempting to extract credentials from db [{CREDS_DB_PATH}].')
        if not CREDS_DB_PATH.exists():
            print(f'Persistence storage does not currently exist under [{CREDS_DB_PATH}].')
            return dict()
        with open(CREDS_DB_PATH, 'r') as f:
            data = json.loads(f.readline().rstrip())
            return data

    def store_creds(self, credentials_dict: dict):
        curr_creds = self.get_creds()
        print('POINT HERE:')
        print(curr_creds)
        curr_creds.update(credentials_dict)
        with open('store_tmp.json', 'w') as f:
            f.write(json.dumps(curr_creds))

    def flush_creds(self):
        # with open
        pass

