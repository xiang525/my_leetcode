class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
    	size = len(nums)
    	left, right = 0,size
    	ans = 0
    	while left <= right:
    		mid = (left + right) /2
    		if self.solve(mid,s,nums):
    			ans = mid
    			right = mid -1
    		else:
    			left = mid + 1
    	return ans


   	def solve(self,l,s,nums):
   		sums = 0
   		for i in range(len(nums)):
   			sums += nums[i]
   			if i >= l:
   				sums -= nums[i -l] # 向后移动多少index， 对应的减去前面的index
   			if sums >= s:
   				return True
   		return False


"""
# ********** The Second Time **********
# 解法一：
# O(n)解法：滑动窗口法，使用两个下标start和end标识窗口（子数组）的左右边界
# 注意此题数组是无序的
"""
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):      
      left = right = sums = 0
      size = len(nums)      
      ans = n + 1  # 初始化取一个大于最长长度的值
      while True:
        if sums < s:
          if right >=size:
            break
          sums += nums[right]
          end += 1
        else:
          if left > right:
            break
          ans = min(ans, left-right)
          sums -= nums[left]
          left += 1
      return [0,ans][ans<=size]

"""
# 解法二：
# O(nlogn)解法：二分枚举答案，每次判断的时间复杂度为O(n)
二分法没有双指针法好理解
"""
res = len(nums) + 1
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]  # 这样数组就是递增的了
        
        l = 0
        for i, n in enumerate(nums):
            if nums[i] >= s:
                l = self.findLeft(nums, l, i, n, s)
                res = min(res, i - l + 1)
        
        return res if res <= len(nums) else 0
    
    def findLeft(self, nums, l, r, n, s):  # 理解数组是递增的， 这里就很好理解了
        while l < r:
            mid = l + (r - 1) / 2
            
            if n - nums[mid] < s:  # nums[mid] > n - s (upper bound)
                r = mid
            else:
                l = mid + 1
            
        return l






"""
O(n), 两个指针,很喜欢这种解法
"""
class Solution:

def minSubArrayLen(self, s, nums):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums):
        total += n
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    return result if result <= len(nums) else 0

 # http://bookshadow.com/weblog/2015/05/12/leetcode-minimum-size-subarray-sum/

"""
O(nlogn):有些不是太懂
"""
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right = 0, size
        bestAns = 0
        while left <= right:
            mid = (left + right) / 2
            if self.solve(mid, s, nums):
                bestAns = mid
                right = mid - 1
            else:
                left = mid + 1
        return bestAns

    def solve(self, l, s, nums):
        sums = 0
        for x in range(len(nums)):
            sums += nums[x]
            if x >= l:
                sums -= nums[x - l]
            if sums >= s:
                return True
        return False

"""
jiuzhong solution, O(n),双指针， 视频5—1
i and j 一直向前移动， 追击型指针 
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0; sums = 0; n = len(nums); res = (1<<31)
        for i in range(n):
            while j < n and sums < s:
                sums += nums[j]
                j += 1
            if sums >= s:
                res = min(res,j-i)
            sums -= nums[i]
        if res == (1<<31):return 0
        return res

"""
比较好的写法
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:return 0
        minlen = sys.maxint; j = 0;sums = 0
        for i in range(n):
            while j < n and sums < s:
                sums += nums[j]
                j += 1
            if sums >= s:
                minlen = min(minlen, j-i)
            sums -= nums[i]
        if minlen == sys.maxint:return 0
        return minlen
        



