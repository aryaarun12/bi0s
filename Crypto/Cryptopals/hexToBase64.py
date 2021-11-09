import base64
x = input()
b = bytes.fromhex(x)
print(b)
bb = base64.b64encode(b)
print(bb)
