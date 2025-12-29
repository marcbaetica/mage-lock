import mmh3
from lib.storage_crud import print_persistent_creds
from lib.credentials_sdk import Credentials_SDK


key = 'Test!'
print(key)
print(mmh3.hash(key, signed=False))

print_persistent_creds()

c_sdk = Credentials_SDK()
c_sdk.store_creds('user6', 'lala5')

print_persistent_creds()



# TODO: Clean up below.

from lib.storage_crud import get_creds, post_creds, print_persistent_creds


creds = []
creds.append({'user': 'user1', 'pass': 'lala1'})
creds.append({'user': 'user2', 'pass': 'qwerty1'})
creds.append({'user': 'user3', 'pass': 'more_pass'})
post_creds(creds)

print_persistent_creds()

creds.append({'user': 'user4', 'pass': 'abc123'})
post_creds(creds)

print_persistent_creds()


