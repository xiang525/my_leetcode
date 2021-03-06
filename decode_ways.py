class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
    	if not s or s[0] =='0':
    		return 0
    	dp[0] = 1
    	dp[1] = 1
    	for i in range(2,len(s)+1):
    		if 10<=int(s[i-2:i])<=26 and s[i-1]!='0':
    			dp.append(dp[i-1]+dp[i-2])
    		elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
    			dp.append(dp[i-2])
    		elif s[i-1]!='0':
    			dp.append(dp[i-1])
    		else:
    			return 0
    	return dp[len(s)]

"""
# 解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。状态方程如下：
# 当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），
# 所以dp[i]=dp[i-1]+dp[i-2];
# 当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]
# 当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。
# 注意初始化时：dp[0]=1,dp[1]=1
# 动态规划, 看一位是0还是1~9，看两位是不是在10~26之间。dp[N] = M 表示字符串s的前N位有M种解码方式。
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':  # s[i-1]!='0'排除10和20
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]


"""
我自己的DP模板
要考虑的corner case太多
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0': return 0
        n = len(s); dp = [0]*(n+1)
        dp[0] = 1; dp[1] = 1
        for i in range(2,n+1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1]!= '0':
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp[i] = dp[i-2]
            elif s[i-1]!= '0':
                dp[i] = dp[i-1]
            else:
                return 0
        return dp[n]




