import os,hashlib
from Crypto.Cipher import AES

enc_key = hashlib.sha256("super_secret_key".encode()).digest()[16:]

chipher="067e660e9494571cb81fa477c6eb994185137090fa1ebeba65b2e3b38b661e29a02c2fa381c9c422f0c73873840c28ad".decode('hex')

def decrypt1(msg,key):
    aes_obj = AES.new(key,AES.MODE_ECB)
    return aes_obj.decrypt(msg)

print(decrypt1(chipher,enc_key))	