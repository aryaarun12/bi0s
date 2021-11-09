a = 66528
b= 52920
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b) 
print(gcd(a,b))


