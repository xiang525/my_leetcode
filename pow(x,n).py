"""
# 解题思路：求幂函数的实现。使用递归，类似于二分的思路，解法来自Mark Allen Weiss的
# 《数据结构与算法分析》。
# 别忘了考虑n<0的情况
# recursive
"""
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
    	 if n == 0:
    	 	return 1
    	 elif n < 0:
    	 	return 1/ self.myPow(x,-n)
    	 elif n % 2:
    	 	return self.myPow(x*x,n/2)*x # e.g., n = 5
    	 else:
    	 	return self.pow(x*x,n/2)


