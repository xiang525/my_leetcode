"""
# 用一个栈记录左括号, 右括号和index, 如果当前括号是右括号且栈顶是左括号, 则弹栈并更新maxLen。
# 解题思路：返回括号串中合法括号串的长度。使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，
# 而是未匹配左括号的索引！
# 因为求长度所以stack里存index
O(n) + O(n)
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
    	#if not s: return 0
    	maxLen = 0; stack = [-1]
    	for i in range(len(s)): 
    		
    		if s[i] == ')' and s[stack[-1]]=='(' and stack[-1]!= -1:
    			stack.pop()
    			maxLen = max(maxLen,i - stack[-1]) 
    		else:
    			stack.append(i)   		
    	return maxLen



"""
另一种写法
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]; maxLen = 0# stack[-1]很重要，为了计算长度做了一个巧妙的赋值
        for i in range(len(s)):
            if len(stack) > 1 and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1])# 必须要先弹占
            else:
                stack.append(i)
        return maxLen



"""
采用了动态规划，dp[i]表示以i为子字符串末尾时的最大长度，最后的结果就是dp中的最大值。如果不是空字符串，
则dp[0]=0，因为一个括号肯定无法正确匹配。递推关系是:
) ( ) ( ( ) ) )
0 1 2 3 4 5 6 7
看当前括号的前一个括号的匹配情况，例如在7之前以6结尾的的最佳匹配是3-6，看3之前的括号和7是否匹配，
不匹配则没有变化；而6之前以5结尾的最佳匹配是4-5，此时3和6匹配，则dp[i]+2。此外，如果与当前括号匹配的
左括号之前的括号的dp值也应该加进来，因为由于添加了当前的括号，那些括号也被连接起来了。例如3和6匹配后，
1和2也应该被加到以6结尾的最佳匹配中。
O(n) + O(n) 没用stack
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [0 for i in range(n)]
        for i in range(1, n):
            if s[i] == ")":
                j = i - 1 - dp[i - 1]
                if j >= 0 and s[j] == "(":
                    dp[i] = dp[i - 1] + 2
                    if j - 1 >= 0:
                        dp[i] += dp[j - 1]
        return max(dp)








if __name__ == '__main__':
	a = Solution()
	print a.longestValidParentheses("()(()")

	    	
