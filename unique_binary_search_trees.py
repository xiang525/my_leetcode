"""
# 解题思路：这题从数学上讲，其实是卡特兰数。不过我们显然不从数学上来解决这个问题。这题是求二叉树的棵数。
# 这里有个解题技巧：一般来说求数量，要首先想到使用动态规划（dp），而如果是像下一题的要求，不只是数量，
# 还要把所有的树都枚举出来，就要使用dfs（深度优先搜索）来遍历决策树了。
# 那么这道题是使用动态规划来解决的。那么如何去求这个问题的状态转移方程呢？其实大部分动态规划的难点都是求
# 状态转移方程。n=0时，为空树，那么dp[0]=1; n=1时，显然也是1，dp[1]=1；n=2时，dp[2]=2; 对于n>2时，
# dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]；这不就是卡特兰数的定义吗？
# 直接有定理
# Catalan数： http://blog.csdn.net/hackbuteer1/article/details/7450250
# http://www.cppblog.com/MiYu/archive/2010/08/07/122573.html
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
    	dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)] #dp在前面已被付了3个值，在此基础上延展
            for i in range(3, n + 1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]


"""
以下处理边界的方式也是可以接受的
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """        
        dp = [1,1,2]
        if n <=2:return dp[n]
        dp += [0]*(n-2) #赋值为0 不是1， 因为后面是叠加 没有的话应该为0 才能不叠加没有的
        for i in range(3,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1] #到i时的dp分为两部分， 一部分是i之前的j， 另一部分是从j到i的；两部分相乘
                                           #i-1-j中1是为了减去root
        return dp[n]















