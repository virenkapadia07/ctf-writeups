# Challenge Name
  RSA-signing-sanity-check

# Challenge Description
code that generated the parameters is give.

# Flag 
shellctf{RSA_1s_s0_aw3som3!}

# Category
Easy

# Point
444

# Solution
In this challenge, we are given **n**,**e** and **sign**(i.e chpher text).



def sign(d,n):

      pt = bytes_to_long(flag)
    
      return pow(pt,d,n)

RSA involves a public key and private key. The public key can be known to everyone; it is used to encrypt messages. Messages encrypted using the **public key (e)** can only be decrypted with the **private key (d)** or vice-versa.
By looking the above encryption code we can see that plaintext is encrypted using private key(i.e **d**).

**Note:-** Encryption decryption can't be done with one key.

Therefore we need to decrypt the message using public key(i.e **e**), which is already given to us.

So by doing pow(sign,e,n) we can easly get our paintext.

Decryption code is in **decrypt.py** file.
