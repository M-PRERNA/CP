# count stairs tabulation
def countpaths(n,a):
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1,-1,-1):
        for j in range (1,a[i]+1):
            if (i+j)>n:
                dp[i] += 0
            else:
                dp[i] += dp[i+j]
        
    
    return dp[0]

    
if __name__ == "__main__":
    n = int(input())
    a =[]
    for i in range (0,n):
        a.append(int(input()))
#     count = [0]*(n+1)
    print(countpaths(n,a))
