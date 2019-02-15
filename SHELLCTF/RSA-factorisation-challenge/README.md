# Challenge Name
RSA-factorisation-challenge

# Challenge Description
the flag has been encrypted with the given code and the parameters are given. can you get the flag! flag format : shellctf{some_string}

# Flag 
shellctf{pr1m3_numb3r$_r_c00l!}

# Category
Medium

# Point
480

# Solution
In this challenge, given parameters are n,e,encrypted_flag.
By going through the encryption code, its clear that we need **d** to decrypt the message.
To find **d** we must have to get value of **p**.
We can get value of **p** by factorizing **n**.

Some values of **n** can be factorized with the help of http://factordb.com

Given value of **n** is factorized with the help of http://factordb.com

> So, p=84380714355347151629255168003741763733877356650613922023696285117470567621119

With the help of **p** we can get **d** and get the flag.

Decryption code is in **decrypt.py** file.
