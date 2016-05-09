"""
我自己写的，没参考任何答案 O(n^2)
"""
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums); counter = 0
        nums.sort()
        if n < 3:return counter
        for i in range(n-1):
            j = i+1; k = n-1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < target:                    
                    counter += k - j 
                    j += 1 
                elif sums >= target:
                    k -= 1
        return counter