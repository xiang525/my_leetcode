class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, A):
        length = len(A)
        for i in xrange(length):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > length or A[i] == A[A[i]-1]: break
                # swap A[i], A[A[i]-1]
                t = A[A[i]-1]; A[A[i]-1] = A[i]; A[i] = t
        for i in xrange(length):
            if A[i] != i + 1:
                return i + 1
        return length + 1


    	# http://heai.info/2014-10/markdown-leetcode-first-missing-positive/
    	# A[i] = i + 1 ==> A[i] - 1 = i
    	# ==> A[i] = A[A[i]-1] 
    	# ==> A[A[i]-1] = A[i]

# ***** The Second Time ********
# 题目给出1到N的正整数，但是不全，里面也可能混着0和负整数，找出第一个缺失的正整数。
# 要求时间O(N)空间固定，可使用原数组，通过交换元素使得A[i] = i + 1，第二次遍历时不满足
# A[i] = i + 1的就是要找的数。
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] ! = i + 1:
                if nums[i]<=0 or nums[i] > n or nums[i] == nums[nums[i]-1]:
                    break
                tmp = nums[i]; nums[i] = nums[nums[i]-1] ; nums[nums[i]-1] = tmp
                # 交换元素的推导在上面

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1  #最后一个元素的下一个
        
























