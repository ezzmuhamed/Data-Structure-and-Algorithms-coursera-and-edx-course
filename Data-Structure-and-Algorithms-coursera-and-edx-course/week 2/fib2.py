
# Uses python2

def fib(n):
 if(n <=1):
     return (n)
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a


n = int(input())
print(fib(n))
