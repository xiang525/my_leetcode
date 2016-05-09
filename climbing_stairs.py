    class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
    	
    	dp = [1] * (n+1)
    	for i in range(2,n+1):
    		dp[i] = dp[i-1] + dp[i-2]
    	return dp[n]



# ********** The Second Time********
"""
# Solution: 这道题就是经典的讲解最简单的DP问题的问题。。
# 假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，
# 要不就是从n-2层2步上来的，所以递推公式非常容易的就得出了：
#dp[n] = dp[n-1] + dp[n-2]
"""
class Solution:
    # @param {integer} n
    # @return {integer}
     def climbStairs(self, n):
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

"""
另一种写法， 思路是一样的
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n)]  #初始化全为1
        for i in range(1,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

"""
可以进行空间优化
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
        return dp[n%3]



