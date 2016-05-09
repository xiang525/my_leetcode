"""
O(nk) is not the best solution
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
    	if k > len(nums) or nums == []: return []
    	res = []
    	for i in range(len(nums)+1-k):
    		window = nums[i:i+k]
    		res.append(max(window))
    	return res

if __name__ == '__main__':
	a = Solution()
	print a.maxSlidingWindow([1],1)


# 我自己做的很直白的思想， 最好看下别人的solution

"""
 jiuzhong solution， discussion codes
 O(n);双端队列
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []; deque = []
        for index, value in enumerate(nums):
            if deque and deque[0] + k <= index:
                deque.pop(0)
            while deque and nums[deque[-1]] < value:
                deque.pop()
            deque.append(index)
            if index+1 >= k:
                ans.append(nums[deque[0]])
        return ans

"""
用deque的实现 O(n)
"""
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [];q = deque(); n = len(nums)
        for index in range(n):
            if q and q[0] == index - k:
                q.popleft()
            while q and nums[q[-1]] < nums[index]:
                q.pop()
            q.append(index)
            if index + 1 >= k:
                ans.append(nums[q[0]])
        return ans


