from binascii import unhexlify 
import string
enc="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
enc=unhexlify(enc)
l=len(enc)
x=''
for i in range(256):
	x=b''
	for a in enc:
		x=x+bytes([a^i])
	print(x)
