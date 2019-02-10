# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:40:44 2018

@author: theja
"""
from Crypto.Cipher import AES
import json
from base64 import b64encode
from Crypto.Util.Padding import pad
from base64 import b64decode
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import time
import os

#aes-cbc mode
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

#generation of 16 byte key
start_time = time.clock()
for i in range(1):
    key = get_random_bytes(16)
print("Key generation time: %s seconds" % (time.clock() - start_time))
print("\n---1 KB File----")


#encryption of 1kb file
start_time = time.clock()
for i in range(1):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message_kb.encode("utf-8"), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result_kb = json.dumps({'iv':iv, 'ciphertext':ct})
print("Encryption time for 1 KB file: %s seconds" % (time.clock() - start_time))
print("Encryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))


    
#decryption of 1kb file
start_time = time.clock()
for i in range(1):
    b64 = json.loads(result_kb)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
print("Decryption time 1 KB file: %s seconds" % (time.clock() - start_time))
print("Decryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))

#print(result_kb)
#print(pt)
#above verifies that encrypted text and decrypted text is the same. Commenting this section output to
#make the output presentable .
print("\n---1 MB File----")

#encryption of 1mb file
start_time = time.clock()
for i in range(1):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message_mb.encode("utf-8"), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result_mb = json.dumps({'iv':iv, 'ciphertext':ct})
print("Encryption time for 1 MB file: %s seconds" % (time.clock() - start_time))
print("Encryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))

#decryption of 1kb file
start_time = time.clock()
for i in range(1):
    b64 = json.loads(result_mb)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
print("Decryption time for 1 MB file: %s seconds" % (time.clock() - start_time))
print("Decryption time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))

#print(result_mb)
#print(pt)
#above verifies that encrypted text and decrypted text is the same. Commenting this section output to
#make the output presentable .
