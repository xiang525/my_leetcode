class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, A):
    	max_product = front_max = front_min = A[0]
        for i in xrange(1, len(A)):
            front_max, front_min = max(A[i], A[i]*front_max, A[i]*front_min), min(A[i], A[i]*front_max, A[i]*front_min)
            max_product = max(max_product, front_max, front_min)
        return max_product




"""
# 解题思路：主要需要考虑负负得正这种情况，比如之前的最小值是一个负数，再乘以一个负数就有可能成为一
# 个很大的正数。
此解法最好最直接
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
    	if len(nums)==0: return 0
    	min_tmp = max_tmp = result = nums[0]
    	for i in range(1,len(nums)):
    		a = nums[i] * min_tmp
    		b = nums[i] * max_tmp
    		c = nums[i]
    		max_tmp = max(max(a,b),c)
    		min_tmp = min(min(a,b),c)
    		result = max(max_tmp,result)
    	return result


"""
Solution 2: two tables(DP_max, DP_min) to store the max and min at currenet index i 
by compareing three values(A[i], A[i] * DP_max[-1], A[i] * DP_min[-1]) respectively
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        ps, ns = [nums[0]],[nums[0]]
        for i in range(1,len(nums)):
            tp, np = ps[-1],ns[-1]
            ps.append(max(nums[i],nums[i]*tp,nums[i]*np))
            ns.append(min(nums[i],nums[i]*tp,nums[i]*np))
        return max(ps)


















