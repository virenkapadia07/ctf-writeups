from Crypto.Util.number import *
from Hidden.secret import flag

def sign(d,n):
    pt = bytes_to_long(flag)
    return pow(pt,d,n)

def make_key():
    p = getPrime(128)
    q = getPrime(128)
    n = p*q
    e = 65537
    phin = (p-1)*(q-1)
    d = inverse(e,phin)
    signature = sign(d,n)
    print("Works! Key generated!")
    string = "n = {}\ne = {}\nd = {}\np = {}\nq = {},\nflag = {}\nsign = {}".format(n,e,d,p,q,flag,signature)
    print(string)
    open('RSA-signing-sanity-check-challenge/Hidden/key.txt','w').write(string)
    return n,e,signature

n,e,signature = make_key()
params = "n: {}\ne: {}\nsign: {}".format(n,e,signature)
open('RSA-signing-sanity-check-challenge/params.txt','w').write(params)
print("Saved Parameters!")