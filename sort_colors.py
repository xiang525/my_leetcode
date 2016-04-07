"""
# *********** The Second Time ********
# 解题思路：这道题不允许使用排序库函数。那么最直观的解法是：遍历两遍数组，第一遍对0，1，2计数，
# 第二遍对数组进行赋值，这样是可以ac的。但题目的要求是只使用常数空间，而且只能遍历一遍。那么思路就比较
# 巧妙了。设置两个头尾指针，头指针p0指向的位置是0该放置的位置，尾指针p2指向的位置是2该放置的位置。
# i用来遍历整个数组，碰到0把它和p0指向的数交换，碰到2把它和p2指向的数交换，碰到1继续向后遍历。
# 有点类似快速排序的分割数组这一步。
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
    	if not nums:
    		return 
    	p0 = 0; p2 = len(nums)-1; i = 0
    	while i <= p2:
    		if nums[i] == 0:
    			nums[i],nums[p0] = nums[p0], nums[i]
    			i += 1
    			p0 += 1
    		elif nums[i] == 2:
    			nums[i],nums[p2] = nums[p2],nums[i]
    			p2 -= 1
    		else:
    			i += 1



#  The fourth Time

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums); red = 0; blue = n -1; i = 0
        while i <= blue: #开始错才这里写成 n-1
            if nums[i] == 0:
                nums[i],nums[red] = nums[red],nums[i]
                i += 1
                red += 1
            elif nums[i] == 2:
                nums[i],nums[blue] = nums[blue],nums[i]
                blue -= 1 # ==2时i不变 
                
            else:
                i+=1








