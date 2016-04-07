"""此题要注意从1开始， 从0开始会出问题
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i in range(len(nums)):
            index = d.get(nums[i])
            if index >= 0 and abs(i - index) <= k:
                return True
            d[nums[i]] = i 
        return False
        

if __name__ == '__main__':
	a = Solution()
	print a.containsDuplicate([3,3])