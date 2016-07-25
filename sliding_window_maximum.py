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
我们用双向队列可以在O(N)时间内解决这题。当我们遇到新的数时，将新的数和双向队列的末尾比较，如果末尾比新数小，
则把末尾扔掉，直到该队列的末尾比新数大或者队列为空的时候才住手。这样，我们可以保证队列里的元素是从头到尾降序的，
于队列里只有窗口内的数，所以他们其实就是窗口内第一大，第二大，第三大...的数。保持队列里只有窗口内数的方法
和上个解法一样，也是每来一个新的把窗口最左边的扔掉，然后把新的加进去。然而由于我们在加新数的时候，
已经把很多没用的数给扔了，这样队列头部的数并不一定是窗口最左边的数。这里的技巧是，我们队列中存的是那个
数在原数组中的下标，这样我们既可以直到这个数的值，也可以知道该数是不是窗口最左边的数。这里为什么时间复杂度
是O(N)呢？因为每个数只可能被操作最多两次，一次是加入队列的时候，一次是因为有别的更大数在后面，所以被扔掉，
或者因为出了窗口而被扔掉。
用deque的实现 O(n), space O(n)
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


