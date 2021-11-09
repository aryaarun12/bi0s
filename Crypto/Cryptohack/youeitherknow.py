from binascii import unhexlify

def xor(ip,k):
	s=b''
	for b1,b2 in zip(ip,k):
		s+=bytes([b1^b2])
	return s.decode("utf-8")
x=input()
l1=len(x)
x=unhexlify(x)
d="crypto{"
l2=len(d)
k=xor(x[:l2],d.encode())
kl=len(k)
key=k+"y"
key=key*(int(l1/8))
m=l1%8
key+=key[:m]
key=key.encode()
f=xor(x,key)
print(f)
