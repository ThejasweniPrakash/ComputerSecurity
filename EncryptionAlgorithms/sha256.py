# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:43:33 2018

@author: theja
"""

from Crypto.Hash import SHA256
import time
import os

file_kb = open("dummy_1KB.txt", "r")
file_mb = open("dummy_1MB.txt", "r")

#reading the file
message_kb = file_kb.read();
message_mb = file_mb.read();

filesize_kb = os.path.getsize("dummy_1KB.txt")
filesize_mb = os.path.getsize("dummy_1MB.txt")
print("-----1 KB File-----")

h = SHA256.new()
f = open("dummy_1KB.txt", "r")
start_time = time.clock()

for i in range(1):
    h.update(message_kb.encode("utf-8"))
print("SHA256 time for 1 KB file: %s seconds" % (time.clock() - start_time))
print("SHA256 time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_kb))
print ("\n")
print (h.hexdigest())



print("\n-----1 MB File-----")

h = SHA256.new()
f = open("dummy_1MB.txt", "r")
start_time = time.clock()

for i in range(1):
    h.update(message_mb.encode("utf-8"))
print("SHA256 time for 1 MB file: %s seconds" % (time.clock() - start_time))
print("SHA256 time for 1 byte: %s seconds" %((time.clock() - start_time)/filesize_mb))
print ("\n")
print (h.hexdigest())