
# Uses python2

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


a,b = raw_input().split()
a = int(a)
b = int(b)
print(lcm(a, b))
