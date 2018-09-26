def last_digit_fast(n):
    if n<=1 :
        return n
    a,b = 1,1
    for i in range(n-1):
        a,b = b,(a+b)%10
    return(a)

n = int(input())
print(last_digit_fast(n))
