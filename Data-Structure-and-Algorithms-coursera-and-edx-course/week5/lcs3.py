
#uses python2
def lcs3(a, b, c):
	
	dp = [[[0 for k in range(len(c)+1)] for j in range(len(b)+1)] for i in range(len(a)+1)]
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			for k in range(1,len(c)+1):
				if a[i-1]==b[j-1] and b[j-1] == c[k-1]: dp[i][j][k] = dp[i-1][j-1][k-1] + 1
				else:
					dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
	return dp[len(a)][len(b)][len(c)]


n = int(input())
a = raw_input()
a = [int (x) for x in a.split()]
u = int(input())
b = raw_input()
b = [int (z) for z in b.split()]
z = int(input())
c = raw_input()
c = [int (y) for y in c.split()]
print(lcs3(a, b, c))
