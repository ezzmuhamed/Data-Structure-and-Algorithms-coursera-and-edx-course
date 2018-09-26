
# Uses python2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a,b = raw_input().split()
a = int(a)
b = int(b)

print(gcd(a, b))
