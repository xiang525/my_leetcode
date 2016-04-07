class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
    	if len(prices) <= 1:
    		return 0
    	low = prices[0]
    	maxProfit = 0

    	for i in range(len(prices)):
    		if prices[i] < low:
    			low = prices[i]
    		maxProfit = max(prices[i] - low , maxProfit)
    	return maxProfit


"""
subarray的思想prefix sum, 但要注意初始化
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:return 0
        profit = 0;min_value = prices[0]
        for i in range(len(prices)):
            min_value = min(min_value,prices[i])
            profit = max(profit,prices[i]-min_value)            
        return profit