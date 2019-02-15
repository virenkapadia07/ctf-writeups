# Challenge Name
Baby-RSA-Challenge

# Challenge Description
URL = http://:/api/Baby-RSA-challenge/

ip : 18.222.210.252 port : 6660 data type: int sign the string **"admin"** with the given RSA Key, and make a GET request to the given URL to get the flag.

# Flag 
shellctf{y0u_sure_kn0w_h0w_RSA_w0rk$}

# Category
Medium

# Point
451

# Solution
As its written in Challenge Description that we have string **"admin"** and we have to sign int using RSA key.
i.e we have to encrypt string **"admin"** using RSA key.
After encrypting the string we have to submit that the output website,

http://18.222.210.252:6660/api/Baby-RSA-challenge/<output>

If the data is correct it will return flag.

All the parameters were given to us.
As there were two keys e and d given to us of we have to encrypt string "admin" with both, to check which one is correct

First I encrypt the string using **e**

	msg="admin"

	encrypt=pow(bytes_to_long(msg),e,n)
	
> Output for above key(e) is **10841810490181526238**

Submiting the output: http://18.222.210.252:6660/api/Baby-RSA-challenge/10841810490181526238

It returned invalid output

So now its clear that the key is **d**.

	msg="admin"

	encrypt=pow(bytes_to_long(msg),d,n)

> Output for above key(d) is **3032817623030053694**

Submiting the output: http://18.222.210.252:6660/api/Baby-RSA-challenge/3032817623030053694

Yeah!! it returns the flag.

Code for encrypting the string "admin" is given in **encrypt.py**
