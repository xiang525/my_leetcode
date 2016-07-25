"""
in-place with O(n)
把duplicates交换到数组的后面去
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        prev = 0; cur = 1
        while cur < len(nums):
            if nums[prev] == nums[cur]:
                cur += 1
            else:
                nums[prev+1], nums[cur] = nums[cur], nums[prev+1]
                prev += 1
                cur += 1
        return prev+1

"""
注意头尾两个 pointer的解法不能处理下面的情况, 所以要用相邻的两个指针
[1,1,2,3,4,4]
"""
