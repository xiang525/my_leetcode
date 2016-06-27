"""
# 我采用的方法是计算第k个Permutation。 假设n = 6，k = 400, 先计算第一位，
# 第一位为6，那么它最少也是第5! * 5 + 1个排列，这是因为第一位为1/2/3/4/5时，都有5!个排列，因此第一
# 位为6时，至少是第5! * 5 + 1个排列（这个排列为612345）。5! * 5 + 1 = 601 > k，所以第一位不可能是6.
# 一个一个地枚举，直到第一位为4时才行，这时，4xxxxx至少为第5! * 3 + 1 = 361个排列。
# 然后计算第二位，与计算第一位时的区别在于，46xxxx至少为第4! * 4 + 1 = 97个排列，这是因为比6小的只
# 有5/3/2/1了。最后可以计算出第二位为2。
"""

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k): # k是第几个排列
    	res = ''
    	k -= 1
    	fac = 1
    	for i in range(1,n):  # 从1 开始
    		fac * = i  # for （n-1）! 
    	num = [i for i in xrange(1,n+1)]# 从1 开始
    	for i in reversed(xrange(n)):
    		curr = num[k/fac]
    		res += str(curr)
    		num.remove(curr) # 不移去会有重复元素出现
    		if i != 0:
    			k %= fac
    			fac /= i  # e.g., (n-1)!/(n-1) = (n-2)!
    	return res


"""
自己跑test case会很清楚
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """      
        fac = 1
        k -= 1
        res = ''
        for i in range(1,n-1):
            fac *= i  # fac = 1        
        nums = range(1,n+1)  # nums = [1,2]
        for i in reversed(range(n)):            
            cur = nums[k/fac] # cur = nums[0] = 1   
            res += str(cur)  # res = '1'
            nums.remove(cur)  # nums = [2]
            if i:
                k %= fac # k = 1
                fac /= i  # fac = 1
        return res


if __name__ == '__main__':
    a = Solution()
    print a.getPermutation(2,1)

    	








