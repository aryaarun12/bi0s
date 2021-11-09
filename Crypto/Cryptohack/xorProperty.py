from binascii import unhexlify
k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" #k1
k1= int(k1,16) 
b="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" #b=k2^k1
b= int(b,16)
c="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" #c=k2^k3
c= int(c,16)
e="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" #e=f^k1^k2^k3
e= int(e,16)
k2=b^k1
k3=c^k2
d=k3^b
f=hex(e^d)
f=str(f)
f=f[2:]
r= bytearray.fromhex(f).decode("utf-8")
#print(f.decode("hex"))
#r = bytes.fromhex(str(f))
print(f)
print(r)
