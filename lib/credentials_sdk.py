from .constants import CREDS_DB_PATH
from .storage_crud import get_creds, post_creds


class Credentials_SDK:
    def get_creds(self):
        if not CREDS_DB_PATH.exists():
            print(f'Persistence storage does not currently exist under [{CREDS_DB_PATH}].')
            return []
        with open(CREDS_DB_PATH, 'r') as f:
            return [line.rstrip() for line in f.readlines() if len(line) > 0]

    def store_creds(self, username, password):
        cred = dict()
        cred['user'] = username
        cred['pass'] = password
        curr_creds = get_creds()
        curr_creds.append(cred)
        post_creds(curr_creds)

    def flush_creds(self):
        # with open
        pass

