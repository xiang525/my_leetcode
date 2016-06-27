class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
    	length = len(nums)
    	if length == 0:
    		return []
    	if length == 1:
    		return [nums]
    	num.sort()   # after sorting, it's convinent to find duplicates
    	res = []
    	previsouNum = None
    	for i in range(length):
    		if nums[i] == previsouNum:
    			continue
    		previsouNum = nums[i]
    		for j in self.permuteUnique(nums[:i]+nums[i+1:]):
    			res.append([nums[i]]+j)
    	return res



"""
# 解题思路：这道题也是穷举全排列，只是集合中可能有重复的元素。分两步：1，对集合进行排序。2，进行剪枝，
# 如果元素重复，直接跳过这一元素，决策树的这一枝被剪掉。
# 和Permutation那道题目差不多，也是递归，不过要去重。先排序，再利用prevNum变量区分是否重复。
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        n = len(nums)
        if n == 0: return []
        if n == 1: return [nums]
        nums.sort()
        res = []
        preNum = None  # record the previous element

        for i in range(n):
            if nums[i] == preNum:
                continue
            else:
                preNum = nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]): # 经常用的技巧
                res.append([nums[i]] + j)
        return res



"""
The forth time: if you use if ([nums[i]]+j) not in ans:
                    ans.append([nums[i]]+j)
will have time out problem. Because the if statment is time consuming. 
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums);ans = []
        if n == 0:return []
        if n == 1: return [nums]
        nums.sort()
        preNum = None

        for i in range(n):
            if nums[i] == preNum:
                continue
            else:
                preNum = nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                ans.append([nums[i]]+j)
        return ans
            


"""
模板解法， 赞一个，一直困惑的超时问题解决了
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,value):
            if len(value) == size:
                ans.append(value)
                return
            for i in range(len(nums)):
                if i and nums[i] == nums[i-1]: #关键在这里
                    continue
                dfs(nums[:i]+nums[i+1:],value+[nums[i]])
                
        ans = []
        if not nums: return ans
        size = len(nums)
        nums.sort()
        dfs(nums,[])
        return ans


























