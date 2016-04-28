    class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, A):
    	step = A[0]
    	for i in range(len(A)):
    		if step > 0:
    			step -= 1
    			step = max(step,A[i])
    		else:
    			return False
    	return True

"""
# 问能否跳最后一个位置，可以将问题转换为跳到最后一个位置后剩余的最大步数（如果不能跳到，提早结束程序)。
# 通过求到每个位置剩余的最大步数可求到最后一个位置的剩余的最大步数。
# 设 step = A[0]，到下一个位置时，step--，并且step = max(step, A[1]);
# 复杂度：时间O(n)，空间O(1)
"""

# ********* The Second Time ***************
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        step = nums[0]
        for i in range(1,len(nums)):
            if step > 0:
                step -= 1
                step = max(step,nums[i]) #不是累加， 跳到一个新地方的时候， 前面的都废了， 要重新计算step
            else:
                return False
        return True
        



"""
greedy, 九章solution
"""
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:return False
        farthest = nums[0]
        for i in range(1,len(nums)):
            if i <= farthest and nums[i] + i >= farthest:
                farthest = nums[i] + i 
        return farthest >= len(nums)-1

        

"""
论坛里的方法， 个人比较喜欢；Greedy的解法
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxValue = 0
        for i in range(len(nums)):
            if maxValue < i:# 只有前面又一次达到 > i就可以了
                return False
            maxValue = max(maxValue,i+nums[i]) # 最大值每次jump后都会更新
        return True



"""
DP 做法： yes or no 可以往DP想
水中的鱼的解法： http://fisherlei.blogspot.com/2012/12/leetcode-jump-game.html
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = 0
        for i in range(1,n):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i]< 0:
                return False            
        return dp[n-1] >= 0


"""
序列型dp的解法超时 O(n^2)
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False for i in range(n)]
        dp[0] = True
        for i in range(1,n):
            for j in range(i):
                if dp[j] and (j + nums[i] >= i):
                    dp[i] = True
                    break
        return dp[n-1]












