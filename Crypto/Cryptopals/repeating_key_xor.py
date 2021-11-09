import binascii
import string 

s="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
l=len(s)
x='0'
s=bytes(s,'utf-8')
print(s)
key=b'ICE'
print(key)
a=0
for i in s:
	#print(i)
	if(a==0):
		h=hex(key[a]^i)
		h=h[2:]
		#x=x+(hex(key[a]^i))
		x=x+h		
		a=1
	elif(a==1):
		h=hex(key[a]^i)
		h=h[2:]
		#x=x+(hex(key[a]^i))
		x=x+h
		a=2
	elif(a==2):
		h=hex(key[a]^i)
		h=h[2:]
		#x=x+(hex(key[a]^i))
		x=x+h
		a=0
print(x)
