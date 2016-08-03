"""
math solution
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)


"""
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ (i+1) ^ nums[i]
        return xor
