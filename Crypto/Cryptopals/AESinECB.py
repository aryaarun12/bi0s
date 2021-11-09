>>> import base64
>>> with open('z.txt') as f:
...         ciphertext = base64.b64decode(f.read())
...
>>> key = b'YELLOW SUBMARINE'
>>> from Crypto.Cipher import AES
>>> key = b'YELLOW SUBMARINE'
>>> cipher = AES.new(key, AES.MODE_ECB)
>>> plaintext = cipher.decrypt(ciphertext)
>>> plaintext
