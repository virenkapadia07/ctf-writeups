from Crypto.Util.number import *
from Hidden.secret import flag

def encrypt(pt,e,n):
    pt = bytes_to_long(pt)
    return pow(pt,e,n)

def decrypt(ct,d,n):
    pt = pow(ct,d,n)
    return long_to_bytes(pt)

def make_key():
    p = getPrime(256)
    n = p*p
    e = 65537
    phin = (p-1)*(p)
    d = inverse(e,phin)
    enc_flag = encrypt(flag,e,n)
    dec_flag = decrypt(enc_flag,d,n)
    assert (flag == dec_flag) , "e,phin not coprime!"

    print("Works! Key generated!")
    string = "n = {}\ne = {}\nd = {}\np = {}\nencrypted flag = {}\ndecrypted flag = {}\n".format(n,e,d,p,enc_flag,dec_flag)
    print(string)
    open('RSA-factorisation-challenge/Hidden/key.txt','w').write(string)

    return n,e,enc_flag

n,e,signature = make_key()
params = "n : {}\ne : {}\nencrypted_flag : {}\n".format(n,e,signature)
open('RSA-factorisation-challenge/params.txt','w').write(params)
print("Saved Parameters!")