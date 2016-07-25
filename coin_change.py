"""
论坛里的解法 Dynamic programming with dp[i] telling the number of coins needed for amount i.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount + 1] * amount
        for c in coins:
            for i in xrange(c, amount+1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] <= amount else -1
                    



"""
另一种写法
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount+1]*amount
        for c in coins:
            for i in xrange(c,amount+1):
                dp[i] = min(dp[i],dp[i-c]+1)
        return dp[amount] if dp[amount] <= amount else -1


"""
DFS 解法
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.minValue = sys.maxint
        coins.sort(reverse=True)
        
        def dfs(start, remain, count):
            if remain == 0:
                self.minValue = min(self.minValue, count)
            for i in range(start, len(coins)):
                if coins[i] <= remain < coins[i] * (self.minValue - count):# optimization for time
                    dfs(i, remain-coins[i], count+1)
                    
        for i in range(len(coins)):
            dfs(0,amount,0)
        return self.minValue if self.minValue < sys.maxint else -1




        