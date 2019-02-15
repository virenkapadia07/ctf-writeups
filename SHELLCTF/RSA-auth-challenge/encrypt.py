from Crypto.Util.number import *

p=305642922468679253888750508455000561549
q=p
e = 65537
n=93417596055195077498335379692060012888951573237753710434943544793905337279401
phin = (p-1)*(q)
d = inverse(e,phin)
msg="admin"
msg=bytes_to_long(msg)

encrypt=pow(msg,d,n)
print(encrypt)