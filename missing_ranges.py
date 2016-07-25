"""
O(n)
prev 用来记录前一个range的结束位置
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        nums.append(upper+1)
        pre = lower - 1
        for curr in nums:
           if (curr == pre + 2):
               result.append(str(curr-1))
           elif (curr > pre + 2):
               result.append(str(pre + 1) + "->" + str(curr -1))
           pre = curr
        return result