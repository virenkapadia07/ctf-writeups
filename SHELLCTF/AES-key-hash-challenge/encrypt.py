import os,hashlib
from Crypto.Cipher import AES
from Hidden.secret import flag,secret_decrypt_function

enc_key = hashlib.sha256("super_secret_key".encode()).digest()[16:]

print("Encryption key : {}".format(enc_key.hex()))

def encrypt(msg,key):
    aes_obj = AES.new(key,AES.MODE_ECB)
    return aes_obj.encrypt(msg.encode())
    
ciphertext = encrypt(flag,enc_key)
assert flag == secret_decrypt_function(ciphertext,enc_key) 

string = "Ciphertext     : {} ".format(ciphertext.hex())
print(string)
open('AES-key-hash-challenge/params.txt','w').write(string)