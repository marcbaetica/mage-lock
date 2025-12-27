from lib.storage_crud import get_creds, post_creds


class Credentials_SDK:
    def store_creds(self, username, password):
        cred = dict()
        cred['user'] = username
        cred['pass'] = password
        curr_creds = get_creds()
        curr_creds.append(cred)
        post_creds(curr_creds)

    def flush_creds(self):
        pass

