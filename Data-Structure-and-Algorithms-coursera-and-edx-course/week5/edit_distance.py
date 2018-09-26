
#uses python2

def edit_distance(s, t):
	
	m , n = len(s) , len(t)
	dp=[[0 for i in range(n+1)] for j in range(m+1)]
	#print dp
	for i in range(m+1): dp[i][0]=i
	#print dp
	for j in range(n+1): dp[0][j]=j;
	#print dp
	for i in range(1,m+1):
		for j in range(1,n+1):
                        #print min(dp[i-1][j-1] + (0 if s[i-1]==t[j-1] else 1)
		 	dp[i][j]=min(dp[i-1][j-1] + (0 if s[i-1]==t[j-1] else 1) , 
						min(dp[i-1][j]+1,dp[i][j-1]+1) )
	return dp[m][n]


s = raw_input()
t = raw_input()
print (edit_distance(s, t))
