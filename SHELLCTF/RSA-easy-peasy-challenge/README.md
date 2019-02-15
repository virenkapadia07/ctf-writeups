# Challenge Name
RSA-easy-peasy-challenge

# Challenge Description
Everything is given. analyze the code and get the flag!

# Flag 
shellctf{y0u_kn0w_RSA!_h0w_coo1_i5_th@t!}

# Category
Medium

# Point
489

# Solution
In this challenge, our flag is divided into two parts i.e flag1 and flag2.

All the parameters are given.

flag1 is encrypted using key **e** and flag2 using key **d**.

Simply decrypt flag1 with **d** and flag2 with **e**.

By joining flag2 and flag1 with get our flag.

Decryption code in present in **decrypt.py** file.
