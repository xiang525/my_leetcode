class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
    	m = len(grid)
    	n = len(grid[0])
    	dp = [[0 for i in range(n)] for j in range(m)]
    	dp[0][0] = grid[0][0]

        # 处理特殊情况， 边界case 不能用后面的统一公式所以要单独处理
    	for i in range(1,n):
    		dp[0][i] = dp[0][i-1] + grid[0][i]

    	for i in range(1,m):
    		dp[i][0] = dp[i-1][0] + grid[i][0]

    	for i in range(1,m):
    		for j in range(1,n):
    			dp[i][j] = min(dp[i][j-1],dp[i-1][j-1]) + grid[i][j]
    	return dp[m-1][n-1]


"""
九章solution: Matrix DP
"""
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid); n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0] #理解含义--从[0][0]到[i][0]只能往下走

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]#理解含义--从[0][0]到[0][j]只能往右走

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


















