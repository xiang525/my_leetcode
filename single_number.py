"""
不是最优解， 因为用了额外的空间
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	d = {}
    	for i in range(len(nums)):
    		if nums[i] not in d:
    			d[nums[i]] = 1
    		else:
    			d[nums[i]] += 1
    	for key in d:
    		if d[key] == 1:
    			return key



"""
# ******** 优化的解法 **********
#很简单，就是位操作，任意两个相同的数如果做异或(Exclusive Or)运算的话，结果为0.所以，
# 这题的解法就是这么直白，从0开始到n，一路异或下去，最后剩下的值就是所求。
""" 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
     
        ans = 0
        for i in range(0,len(nums)):
            ans = ans ^ nums[i] 
        return ans









        