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




        