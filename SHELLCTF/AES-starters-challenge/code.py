#!/bin/usr/python3
import os
from Crypto.Cipher import AES
from Hidden.secret import flag,decrypt_function

enc_key = os.urandom(16)

def encrypt(msg,key):
    aes_obj = AES.new(key,AES.MODE_ECB)
    return aes_obj.encrypt(msg.encode())
    
ciphertext = encrypt(flag,enc_key)

assert flag == decrypt_function(ciphertext,enc_key) 

string = "Ciphertext     : {} \nEncryption Key : {}".format(ciphertext.hex(),enc_key.hex())

print(string)

open('AES-sanity-check-challenge/params.txt','w').write(string)