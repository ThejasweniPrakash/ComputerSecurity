# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:17:37 2018

@author: theja
"""

from Crypto.Hash import SHA512
import time,os

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
filesize_kb = os.path.getsize("dummy_1KB.txt")
filesize_mb = os.path.getsize("dummy_1MB.txt")
print("-----1 KB File-----")

h = SHA512.new()
f = open("dummy_1KB.txt", "r")
start_time = time.clock()

for i in range(1):
    h.update(message_kb.encode("utf-8"))
print("SHA512 time for 1 KB file: %s seconds" % (time.clock() - start_time))
print("SHA512 time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))
print ("\n")
print (h.hexdigest())



print("\n-----1 MB File-----")

h = SHA512.new()
f = open("dummy_1MB.txt", "r")
start_time = time.clock()

for i in range(1):
    h.update(message_mb.encode("utf-8"))
print("SHA512 time for 1 MB file: %s seconds" % (time.clock() - start_time))
print("SHA512 time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))
print ("\n")
print (h.hexdigest())