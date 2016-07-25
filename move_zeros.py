class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0; n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1