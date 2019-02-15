from Crypto.Util.number import *

d = 1855662429992509525
n = 12061805802038279471
e = 13

msg="admin"
chipher=pow(bytes_to_long(msg),d,n)
print(chipher)