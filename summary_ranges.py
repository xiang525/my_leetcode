"""
# 两个指针 start, end.  如果nums[end+1] = nums[end]+1, 就移动end指针, 
否则, 插入字符串nums[start]->nums[end]. 
"""
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
    	res = []
    	begin, end = nums[0],nums[0]
    	for i in range(len(nums)-1):
    		
    		if i < len(nums) and nums[i+1] == nums[i] + 1:    			
    			end = nums[i] 
    		else:
    			interval = str(begin)
    		if begin != end:   		
    			interval += str(begin)+'->'+str(end)
    		res.append(interval)
    		if i < len(nums):
    			begin = end = nums[i]
    		
    	return res


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        start, end = nums[0],nums[0]
        res = []
        for i in range(len(nums)-1):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                interval = nums[i]
                if start != end:
                    interval += "->"+str(end)
                res.append(interval)
                if start == end:
                    start = end = nums[i]
        return res



# *********** My Own Solution ************
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        n = len(nums)
        
        if not nums: return ans
        if n == 1: return [str(nums[0])]
        start = end = 0;interval = ''
        while end <= n-1:
            if end+1 < n and (nums[end+1]) == nums[end] + 1:
                end += 1
                continue
                   
            else:
                if start != end:
                    interval = str(nums[start])+'->' +str(nums[end])
                else:
                    interval = str(nums[end])             
                
                ans.append(interval)
            end += 1
            start = end
            
        return ans



"""
另一种写法
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums); ans = []
        begin = 0; end = 0
        if n == 1: return [str(nums[0])]; tmp = ''
        while end <= n-1:
            while end < n-1 and nums[end]+1 == nums[end+1]:
                end += 1
            if begin == end:
                tmp = str(nums[begin])
            else:
                tmp = str(nums[begin]) + '->' + str(nums[end])
            ans.append(tmp)
            begin = end + 1
            end = begin
        return ans
















