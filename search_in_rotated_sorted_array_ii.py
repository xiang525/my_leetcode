class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, A, target):
        left=0; right=len(A)-1
        while left<=right:
            mid=(left+right)/2
            if A[mid]==target: return True
            if A[left]==A[mid]==A[right]:  # 相等时左右同时移动指针
                left+=1; right-=1
            elif A[left]<=A[mid]:
                if A[left]<=target<A[mid]: right=mid-1
                else: left=mid+1
            else:
                if A[mid]<=target<A[left]: left=mid+1
                else:right=mid-1
        return False


        
"""
用二分法模板的方法: O(nlogn) is too large, not fast enough
此题无法优化到O(n)
// it ends up the same as sequential search
// We used linear search for this question just to indicate that the 
// time complexity of this question is O(n) regardless of binary search is applied or not.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:return False
        nums.sort()
        start = 0; end = len(nums)-1
        while start + 1 < end:
            m = (start + end)/2
            if nums[m]==target:return True
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
            return True
        if nums[end] == target:
            return True
        return False


"""
正确的做法
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
       
        if not nums:return False
        n = len(nums)
        left = 0; right = n-1
        while left+1 < right:
            mid = (left+right)/2
            if nums[mid] == target:return True
            while mid <= right and nums[mid] == nums[right]: #两者取其一即可
                  right -= 1
            # while left < mid and nums[mid] == nums[left]:
            #      left += 1
                
            if nums[left] <= nums[mid]:
                if nums[left]<= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid                
                
                
        if nums[left] == target:return True
        elif nums[right] == target:return True
        return False


        















