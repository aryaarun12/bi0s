a = input()
f = ''

for c in a:
    f += chr(ord(c) ^ 13)
print(f)
