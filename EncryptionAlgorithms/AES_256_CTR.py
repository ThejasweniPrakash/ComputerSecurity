# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:42:12 2018

@author: theja
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:23 2018

@author: theja
"""
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time
import os

file_kb = open("dummy_1KB.txt", "r")
file_mb = open("dummy_1MB.txt", "r")
#dummy_1KB and dummy_1MB files were created using command line argument
    #echo "This is just a sample line appended to create a big file.. " > dummy_1KB.txt
    #for /L %i in (1,1,1) do type dummy.txt >> dummy_1KB.txt
    #echo "This is just a sample line appended to create a big file.. " > dummy_1MB.txt
    #for /L %i in (1,1,14) do type dummy.txt >> dummy_1MB.txt
#File is stored in the same directory as the program

#reading the file
message_kb = file_kb.read();
message_mb = file_mb.read();

#reading the file size: used to calcute time for byte encryption and decryption
filesize_kb = os.path.getsize("dummy_1KB.txt")
filesize_mb = os.path.getsize("dummy_1MB.txt")

#generation of 32 byte key
start_time = time.clock()
for i in range(1):
    key = get_random_bytes(32)
print("Key generation time: %s seconds" % (time.clock() - start_time))


print("\n---1 KB File----")
start_time = time.clock()
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(message_kb.encode("utf-8"))
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result_kb = json.dumps({'nonce':nonce, 'ciphertext':ct})
print("Encryption time for 1 KB file: %s seconds" % (time.clock() - start_time))
print("Encryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))

import json
from base64 import b64decode
from Crypto.Cipher import AES

start_time = time.clock()
b64 = json.loads(result_kb)
nonce = b64decode(b64['nonce'])
ct = b64decode(b64['ciphertext'])
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
pt = cipher.decrypt(ct)
print("Decryption time 1 KB file: %s seconds" % (time.clock() - start_time))
print("Decryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))


print("\n---1 MB File----")
start_time = time.clock()
cipher = AES.new(key, AES.MODE_CTR)
ct_bytes = cipher.encrypt(message_mb.encode("utf-8"))
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result_mb = json.dumps({'nonce':nonce, 'ciphertext':ct})
print("Encryption time for 1 MB file: %s seconds" % (time.clock() - start_time))
print("Encryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))

start_time = time.clock()
b64 = json.loads(result_mb)
nonce = b64decode(b64['nonce'])
ct = b64decode(b64['ciphertext'])
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
pt = cipher.decrypt(ct)
print("Decryption time 1 MB file: %s seconds" % (time.clock() - start_time))
print("Decryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))
