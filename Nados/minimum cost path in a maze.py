# minimum cost path dp in a matrix / maze

def mincostmaze(maze,n,m):
    dp = [[0]*(m+1)]*(n+1)
    for i in range (n-1,-1,-1):
        for j in range (m-1,-1,-1):
            #last cell
            if i==n-1 and j==m-1:
                dp[n-1][m-1] = maze[n-1][m-1]
            #last row
            if i==n-1 and j<m-1:
                dp[i][j] = dp[i][j+1]+maze[i][j] 
            #lst column
            if j==m-1 and i<n-1:
                dp[i][j] = dp[i+1][j]+maze[i][j] 
            #remaining cells
            else:
                dp[i][j] = min(dp[i+1][j],dp[i][j+1]) + maze[i][j]
   
    return dp[0][0]

if __name__ == "__main__":
    n = int(input())
    m = int(input())
#     maze = [[0]*(m)]*(n)
    maze=[]
    for i in range(n):
        col = []
        for j in range(m):
            col.append(int(input()))
        maze.append(col)
       
    print(mincostmaze(maze,n,m))
            
