# Challenge Name
RSA-signed-flag-challenge

# Challenge Description
everything you need to get the flag is given. flag format: shellctf{string}

# Flag 
shellctf{aw3some_w0rk_crack1ng_thi$}

# Category
Hard

# Point
521

# Solution
The **make_key()** function generates RSA key.

Looking at **sign()**, it gives the RSA signature of the input string.

RSA signature is different from RSA encoding, it follows
> s = x<sup>d</sup> mod n\
> x = s<sup>e</sup> mod n

We see that 
> key_sign = pow(temp,d,n)\
> temp = pow(key_sign,e,n)

Since *temp* is an md5 hash

Convert temp to hex and decrypt that. 

**Note:** Use any online md5 decrypter

We decrypt it and get our **xor_string** 

> Decrypted **temp** value is **"encryption"**

    xor_string="encryption"

We also see that
> ciphertext = flag ^ xor_string

Therefore
> flag = ciphertext ^ xor_string

This gives us our flag.

Decryption code is given in **decrypt.py** file
