#!/bin/usr/python3
from Hidden.secret import verify_integrity
from Crypto.Util.number import *

def save_key(n,e,d,p,q):
    string = "n = {}\ne = {}\nd = {}\np = {}\nq = {}\n".format(n,e,d,p,q)
    print(string)
    open('Baby-RSA-challenge/Hidden/key.txt','w').write(string)

def generate_key(bits):
    p = getPrime(bits//2)
    q = getPrime(bits//2)
    n = p * q
    e = 13
    phin = (p-1) * (q-1)
    d = inverse(e,phin)
    assert verify_integrity(n,e,d) == True , ' Invalid Key :( '
    save_key(n,e,d,p,q)
    return n,e,d,p,q

n,e,d,p,q = generate_key(64)

params = "n = {}\ne = {}\nd = {}\np = {}\nq = {}".format(n,e,d,p,q)
open('Baby-RSA-challenge/params.txt','w').write(params)