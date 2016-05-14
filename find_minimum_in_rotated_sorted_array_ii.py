class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0; right = n - 1
        while left + 1 < right:
            while left < right and nums[left] == nums[left+1]: #去重处理
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
                
            mid = (left+right)/2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
               
        if nums[left] < nums[right]: return nums[left]
        else:return nums[right]

