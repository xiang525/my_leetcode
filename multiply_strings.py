class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
    	num1 = num1[::-1]; num2 = num2[::-1]
    	array = [0 for i in range(len(num1)+len(num2))]
    	for i in range(len(num1)):
    		for j in range(len(num2)):
    			array[i+j] += int(num1[i]) * int(num2[j])
    	ans = []
    	for i in range(len(array)):
    		digit = array[i] % 10
    		carry = array[i] / 10
    		if i < len(array)-1:
    			array[i+1]+= carry
    		ans.insert(0,str(digit))
    	while ans[0] == '0' and len(ans) > 1:
    		del ans[0]
    	return ''.join(ans)
if __name__ == '__main__':
	a = Solution()
	#  http://www.cnblogs.com/zuoyuan/p/3781515.html


"""
# ********* The Second Time *************
# 解题思路：两个非负数字字符串的相乘。其实就是大数乘法。算法的关键是要先将两个字符串翻转过来，然后按位进行
# 相乘，相乘后的数不要着急进位，而是存储在一个数组里面，然后将数组中的数对10进行求余（%），就是这一位的数，
# 然后除以10，即/10，就是进位的数。注意最后要将相乘后的字符串前面的0去掉.
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = num1[::-1]; num2 = num2[::-1] # 逆序后方便后面的操作
        tmp = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp[i+j] += int(num1[i]) * int(num2[j]) # 如果i+j的值相同则叠加， 这个和手算是一样的逻辑
        ans = []
        for i in range(len(tmp)):
            digit = tmp[i] % 10
            carry = tmp[i] / 10
            if i < len(tmp)-1:  # 下面是i+1， 所以i不能取到len(tmp)-1
                tmp[i+1] += carry  # 不是当前位接受进位是后面一位因为reverse了
            ans.insert(0,str(digit)) # 前面逆序了， 所以这里总是在首部插入,其实就是再reverse回来
        while ans[0]=='0' and len(ans) > 1: # 前面可以有多个0， 所以用while
            del ans[0]
        return ''.join(ans)


def multiply(self, num1, num2):
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join( map(str,res[::-1]) )



"""
论坛里的更简洁的写法， 合二为一
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]; num2 = num2[::-1]
        m = len(num1); n = len(num2)
        ans = [0]*(m+n)
        
        for i in range(m):
            for j in range(n):
                ans[i+j] += int(num1[i]) * int(num2[j])
                ans[i+j+1] += ans[i+j]/10
                ans[i+j] %= 10
        while ans[-1] == 0 and len(ans) > 1:#因为是反的， 所以要看最后一位
            ans.pop()
        return ''.join(map(str,ans[::-1]))#ans都是int所以要变为str
        






















