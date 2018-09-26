# Uses python2

def fibmod(n, m):
    assert 1 <= n <= 10**18, n
    assert 2 <= m <= 10**5, m

    def f(n):
        if n == 0:
            return 0, 1
        else:
            a, b = f(n // 2)
            c = a * (2*b - a) % m
            d = (a**2 + b**2) % m

            if n % 2 == 0:
                return c, d
            else:
                return d, (c + d) % m

    return f(n)[0]

inp = map(int, raw_input().split())
n, m = inp[0], inp[1]

if ( (n >= 1 and n <= 10**18) and (m >= 2 and m <= 10**5) ):
    out = fibmod(n, m)
print out
