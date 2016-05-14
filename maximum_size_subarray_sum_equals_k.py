"""
O(n) use dictionary to store previous sums
"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums); d = {0:-1} #如果不这样记录数组里有sum为0的话就会少计算长度，因为加起来为零=自己本身就可以了
        if not nums: return 0
        sums = 0; maxlen = 0
        for i in range(n):
            sums += nums[i]
            if sums-k in d:
                maxlen = max(maxlen,i- d[sums-k])
            if sums not in d:
                d[sums] = i
        return maxlen