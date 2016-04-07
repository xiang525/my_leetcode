"""此方法很巧妙
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
    	
    	tail = 0
    	for e in nums:
    		if e != val:
    			nums[tail] = e    			
    			tail += 1
    	return tail


"""
Solution 2, 速度慢， 因为要删除元素
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
        


"""
有种错误的解法：len(nums)是动态变化的， 会造成数组越界异常
"""
def removeElement(self, nums, val):
        for i in range(len(nums)):
            if val == nums[i]:
                del nums[i]
        return len(nums)





if __name__ == '__main__':
	a = Solution()
	nums = [4,5,5]
	print a.removeElement(nums,5)