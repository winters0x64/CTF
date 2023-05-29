import requests
import json
from base64 import b64encode, b64decode
import hashlib
import random

def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()

def crack():
    data_cookie = "eyJ1c2VybmFtZSI6ICJ3aW50ZXJzIiwgInVzZXJfdHlwZSI6ICJiYXNpYyJ9"
    hash_cookie  = "1a22f1dae4183bc77aca2ab4e90cddc947dfa276d8c93ebf3ea8a942117f958d"
    r = hex(random.getrandbits(24))[2:]

    data = {
        "username": "winters",
        "user_type": "basic"
    }

    for i  in range(0XFFFFFF):
        print(i)
        r = hex(i)[2:];
        b64data = b64encode(json.dumps(data).encode())
        data_hash = hash(b64data.decode() + r)
        
        if b64data.decode() == data_cookie and data_hash == hash_cookie:
            print("Random value found")
            print(r)
            break
        else:
            if i%1000000 == 0:
                print(i,'`th million passed')

    print(b64data.decode())
    print(data_hash)


def forge():
    data = {
        "username": "winters",
        "user_type": "premium"
    }
    b64data = b64encode(json.dumps(data).encode())
    data_hash = hash(b64data.decode() + "1285b1")

    print(b64data)
    print(data_hash)


#crack() # Cracked got the value as 1285b1
forge()




