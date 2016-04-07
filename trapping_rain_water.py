"""
# 解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开
# 始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], 
# rightmax)-A[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，
# 则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
# height[i]的储水量与前后bar有关， 所以要leftmosthight and rightmax.
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
    	leftmosthigh = [0 for i in range(len(height))]
    	leftmax = 0
    	for i in range(len(height)):
    		if height[i] > leftmax:
    			leftmax = height[i]
    		leftmosthigh[i] = leftmax
    	sum = 0
    	rightmax = 0
    	for i in reversed(range(len(height))):
    		if height[i] > rightmax:
    			rightmax = height[i]
    		if min(rightmax,leftmosthigh[i]) > height[i]:
    			sum += min(rightmax,leftmosthighp[i]) - height[i]
    	return sum



"""
九章solution的实现：two pointers是solution， 实现时从指针值小的那边灌水
强化班视频讲解很好 3-2
"""
class Solution(object):
    def trap(self, bars):
        if not bars or len(bars) < 2:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


















