
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
    	size = len(num)
    	dp = [0] * (size+1)
    	if size:
    		dp[1] = num[0]
    	for i in range(2,size+1):
    		dp[i] = max{dp[i-1],dp[i-2]+num[i-1]}
    	return dp[size]
    		



"""
# ************ The Second Time **********
# Solution: dp[i]表示盗窃前(!!!)i家的最大收益值
# dp[0] = num[0] （当i=0时）
# dp[1] = max(num[0], num[1]) （当i=1时）
# dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当i !=0 and i != 1时）
注意corner cases
这种做法的状态转移方程和最后一种是不一样的， 注意区分
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]


"""
jiuzhang solution搞复杂了
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 0:return 0
        if n >= 1:dp[0] = nums[0]
        if n >= 2:dp[1] = max(nums[0],nums[1])
        if n >= 3:dp[2] = max(nums[0]+nums[2],nums[1])
        if n > 2:
            for i in range(3,n):
                dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp)

"""
第二遍听九章的解法，觉得很好
dp[i] 表示前i个房子中， 偷了第i个房子的，偷到的最大值. 第i个房子确定偷了
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 0:return 0
        if n == 1:return nums[0]
        if n == 2:return max(nums[0],nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,n):
            dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp[n-1],dp[n-2]) #max(dp)要遍历dp，没有实质性改进，所以两种写法都可以



"""
进一步进行空间优化，我们只需要dp的长度为3，非常棒！
九章视频高级班讲得非常好
我们在求i的时候只与i-2和i-3有关，所以只要知道3个状态就可以了，mod 3 
这个叫滚动指针
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 0:return 0
        if n == 1:return nums[0]
        if n == 2:return max(nums[0],nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        dp[2] = max(nums[0]+nums[2],nums[1])
        for i in range(3,n):
            dp[i%3] = max(dp[(i-2)%3],dp[(i-3)%3]) + nums[i]
        return max(dp[(n-1)%3],dp[(n-2)%3])



"""
dp[i]表示第i个房子偷与不偷的最大值
此题状态方程不同写法可以多样
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return max(dp)





       

