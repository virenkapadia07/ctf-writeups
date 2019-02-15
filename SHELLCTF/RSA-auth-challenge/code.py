from Crypto.Util.number import *

def make_key():
    p = getPrime(128)
    q = p
    n = p*q
    e = 65537
    phin = (p-1)*(q)
    d = inverse(e,phin)
    print("Works! Key generated!")
    string = "n = {}\ne = {}\nd = {}\np = {}\nq = {}\n".format(n,e,d,p,q)
    print(string)
    open('RSA-auth-challenge/Hidden/key.txt','w').write(string)
    return n,e

n,e = make_key()
params = "n = {}\ne = {}\n".format(n,e)
open('RSA-auth-challenge/params.txt','w').write(params)
print("Saved Parameters!")