"""
解题思路：
模拟题，循环过程中用set记录每次得到的平方和当出现非1的重复平方和时，返回False
否则，返回True.
此代码非常简洁
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        numSet = set()    #用list也可以, 用来判断有没有重复值出现
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n == 1  	



  



if __name__ == '__main__':
	s = Solution()
	n = 18
	print s.isHappy(n)