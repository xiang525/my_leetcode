"""
DP
the costs[1][0] represent minimum price to paint the second house red plus the 1st house.
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs) == 0: return 0
        n = len(costs)
        for i in range(1,n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][1], costs[i-1][0])
        return min(costs[n-1][0],costs[n-1][1],costs[n-1][2])