#!/bin/usr/python3
from Crypto.Util.number import *
from Hidden.secret import flag,secret_assertion_function

flag1 = flag[20:]
flag2 = flag[:20]

def encrypt(pt,e,n):
    return pow(pt,e,n)

def sign(ct,d,n):
    return pow(ct,d,n)
    
def make_key():
    p = getPrime(256)
    q = getPrime(256)
    n = p*q
    e = 65537
    phin = (p-1)*(q-1)
    d = inverse(e,phin)
    assert pow(pow(25,e,n),d,n) == 25 , "e , phin aren't coprime!!"
    print("Works! Key generated!")
    string = "n = {}\ne = {}\nd = {}\np = {}\nq = {}".format(n,e,d,p,q)
    print(string)
    open('RSA-easy-peasy-challenge/Hidden/key.txt','w').write(string)
    return n,e,d,p,q

n,e,d,p,q = make_key()

enc_flag1  = encrypt(bytes_to_long(flag1.encode()),e,n)
sign_flag2 = sign(bytes_to_long(flag2.encode()),d,n)

verify = secret_assertion_function(enc_flag1,sign_flag2,e,d,n)
print(verify)

assert flag == verify , "Error!"

params = "n = {}\ne = {}\nd = {}\np = {}\nq = {}\nflag1 = {}\nflag2 = {}\n".format(n,e,d,p,q,enc_flag1,sign_flag2)
open('RSA-easy-peasy-challenge/params.txt','w').write(params)
print("Saved Parameters!")