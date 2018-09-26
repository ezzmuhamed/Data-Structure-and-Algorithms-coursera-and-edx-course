
#uses python2

def knapSack(W, wt, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(wt[i-1]+K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][w]

W,n = map(int,raw_input().split())
wt = raw_input()
wt = [int(x) for x in wt.split()]
print knapSack(W , wt, n) 
