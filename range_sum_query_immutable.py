class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = nums
        for i in range(1,len(nums)):
            self.dp[i] += self.dp[i-1]# 相当于前面加了一个零
            
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.dp[j] - self.dp[i-1]
        else:
            return self.dp[j]