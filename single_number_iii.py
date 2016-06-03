"""
jiuzhang 的思想,非常赞！
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        lastBit = xor - (xor&(xor-1))#视频里讲得很好，为什么是这样
        group1 = 0; group2 = 0
        for i in range(len(nums)):
            if (lastBit & nums[i]) == 0:
                group1 ^= nums[i]
            else:
                group2^= nums[i]
        return [group1,group2]


"""
另一种写法
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums); xor = 0
        for i in range(n):
            xor ^= nums[i]
        #lastBit = xor - (xor & (xor -1))
        lastBit = xor & ~(xor-1) # 需要记忆
        group1 = 0; group2 = 0
        for i in range(n):
            if (lastBit & nums[i]) == 0:
                group1 ^= nums[i]
            else:
                group2 ^= nums[i]
        return [group1,group2]






