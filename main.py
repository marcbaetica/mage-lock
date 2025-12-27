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

