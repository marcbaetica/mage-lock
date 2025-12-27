import json
from pprint import pprint


def get_creds():
    with open('store_tmp.json', 'r') as f:
        data = f.readlines()[0].rstrip()
    return json.loads(data)


def post_creds(creds):
    with open('store_tmp.json', 'w') as f:
        f.write(json.dumps(creds))


def print_persistent_creds():
    latest_creds = get_creds()
    print('Uploaded creds:')
    pprint(latest_creds)

