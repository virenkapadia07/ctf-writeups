import os
from Crypto.Cipher import AES

def decr(msg,key):
    aes_obj = AES.new(key,AES.MODE_ECB)
    return aes_obj.decrypt(msg)
	
msg="b1e2a65b0778a6032d7c899f7f2833e3320df81d21a25c73e12d7d2511be0a1f0387570d1698d63dde9e8673c5766401".decode('hex')
key="c4cd27c9945287587ac15b68859442bf".decode('hex')

print(decr(msg,key))