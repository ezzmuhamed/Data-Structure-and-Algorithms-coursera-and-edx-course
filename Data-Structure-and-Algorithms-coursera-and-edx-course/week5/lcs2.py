
#uses python2

def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 
  
  
# Driver program to test the above function 
n = int(input())
X = raw_input()
X = [int (x) for x in X.split()]
u = int(input())
Y = raw_input()
Y = [int (z) for z in Y.split()]
print  lcs(X , Y, len(X), len(Y)) 
