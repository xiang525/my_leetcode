class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
    	if not nums:
    		return []
    	if len(nums) == 1:
    		return [nums]

    	res = []
    	for i in range(len(nums)):
    		print 'i:',i,nums[:i]+nums[i+1:]

           	for j in self.permute(nums[:i] + nums[i+1:]): # except nums[i]
           		
           		res.append([nums[i]] + j)
        return res

if __name__ == '__main__':
	a = Solution()
	print a.permute([1,2,3])


"""
# ******* The Second Time *********
# 解题思路：穷举一个集合的全排列。这个就是python递归巧妙的使用了。
# 把一个数组拆成两部分的思想经常使用
# 此解法非常巧妙,仔细想想很有意思
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
      if len(nums) == 0: return []
      if len(nums) == 1: return [nums]
      res = []
      for i in range(len(nums)):
        for j in self.permute(nums[:i] + nums[i+1:]):  # 没有nums[i]；巧妙在此处
          res.append([nums[i]] + j)
      return res

"""
discuss里看到的用DFS实现的方法
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,value): 
            if len(nums) == 0:  # 这个条件一开始写错了          
                ans.append(value)                
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],value+[nums[i]])
        ans = []
        dfs(nums,[])
        return ans


"""
也可以用size 
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,value):
            if len(value) == size:
                ans.append(value)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],value+[nums[i]])
        
        ans = []
        size = len(nums)
        dfs(nums,[])
        return ans



      
     
























