class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*n
        #dp[0] = 1; dp[1] = 1; dp[2] = 2
        dp=[1,1,2]
        if n <=2:return dp[n]
        dp += [0]*(n-2) 
        for i in range(3,n):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]



if __name__ == '__main__':
    a = Solution()
    print a.numTrees(4)







