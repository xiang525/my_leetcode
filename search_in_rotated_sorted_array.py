class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
    	left = 0; right = len(nums) - 1
    	while left <= right:
    		mid = (left + right)/2
    		if nums[mid] == target:
    			return mid
    		if nums[mid] >= nums[left]:
    			if target > nums[left] and target < nums[mid]:
    				right = mid - 1
    			else:
    				left = mid + 1
    		elif nums[mid] < nums[right]:
    			if target > nums[mid] and target < nums[right]:
    				left = mid + 1
    			else:
    				right = mid -1
    	return -1

"""
# ******* The Second Time *******
# 解题思路：二分查找的变种。分别讨论左边单调递增还是右边单调递增.
# As the sequence is rotated, for any mid element, either it is of order with its 
# previous part, or it is of order with its next part. e.g. 561234, middle element 
# 1 has an order with its next part 1234.
# 5678123, middle element 8 has an order with its previous part 5678.
# Normal binary search just compare the middle element with the target, here we need 
# more than that.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        left = 0; right = len(nums)-1
        while left < right:
            mid = (left + right)/2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left]<= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1




"""
 九章模板: mid 和start比较来决定 > m 的值实在左边还是右边， 两种情况是相反的
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return -1
        start = 0; end = len(nums)-1
        while start + 1 < end:
            m = (start + end)/2
            if nums[m]==target:return m
            if nums[start] < nums[m]:
                if nums[start] <= target and target <= nums[m]:
                    end = m
                else:
                    start = m
            else:
                if nums[m] <= target and target <= nums[end]:
                    start = m
                else:
                    end = m
        if nums[start] ==  target:
            return start
        if nums[end] == target:
            return end
        return -1
















