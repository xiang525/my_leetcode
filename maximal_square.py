class Solution:
    # @param {character[][]} matrix
    # @return {integer}
     def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for x in range(m)]
        ans = 0
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])
                if x and y and dp[x][y]:
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1 
                ans = max(ans, dp[x][y])
        return ans * ans

# [x][y] is the upper right point


#  ********** The Second Time ********
"""
# DP
# dp[x][y]表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）
jiuzhang视频强化班思路讲得很好
以下代码的写法非常好
"""


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == []: return 0
        m = len(matrix); n = len(matrix[0])
        dp = [[0]*n for x in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j]) # matrix 是string类型的
                if i and j and dp[i][j]: # 省去了判断i,j的范围
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1 # square should be the smallest one
                ans = max(ans, dp[i][j])
        return ans * ans



"""
my own solution
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:return 0
        m = len(matrix); n = len(matrix[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        ans = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            
        for j in range(n):
            dp[0][j] =  int(matrix[0][j])
            
        for i in range(1,m):
            for j in range(1,n):
                if int(matrix[i][j]) == 0:
                    dp[i][j] = 0                    
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        ans = max([max(i) for i in dp])
             
        return ans*ans 


"""
另一种写法
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix); n = len(matrix[0]); ans = 0
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j])  == 0:
                    dp[i][j] = 0
                elif i and j:# i, j为0会有负的index
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                ans = max(ans, dp[i][j]) # 这里比较的时候考虑了 i==0 and j==0的情况，所以m和n从0开始
        return ans**2
        













