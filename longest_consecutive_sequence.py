"""
# 我的思想方法是对的， 但是不能完整地写出代码
# 用dictionary, get item的平均时间复杂度为O(1), 可以把key设为list中的数, value用于标记是
# 否访问过。遍历所有的key, 不断找寻其+1和-1得到的值是否在dictionary中, 记下最长的连续序列长度。
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
    	d = {x:False for x in nums}
    	count = -1
    	for i in d:
    		if d[i] == False:
    			curr = i + 1; lenright = 0
    			while curr in d:
    				lenright += 1; d[curr] = True; curr += 1
    			curr = i -1; lenleft = 0
    			while curr in d:
    				lenleft += 1; d[curr] = True; curr -= 1
    			count = max(count,lenleft+1+lenright)
    	return count


"""
jiuzhang solution: use hash 
用每个元素进出数据结构的次数来判断时间复杂度
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict(); n = len(nums); longest = 0
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
        
        for i in range(n):
            down = nums[i]-1
            while down in d:
                del d[down]  #删除对应的元素就不用重复计算
                down -= 1
            up = nums[i]+1
            while up in d:
                del d[up]
                up += 1
            longest = max(longest,up-down-1)
        return longest



    		


    		

