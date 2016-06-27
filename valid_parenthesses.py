class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	paren_map = {
    	'(':')',
    	'{':'}',
    	'[':']'
    	}
    	stack = []
    	for p in s:
    		if p in paren_map:
    			stack.append(paren_map[p])
    		else:
    			if not stack or stack.pop()!=p:
    				return False
    	return not stack  # as stack is empty == False but we need to return True

# *************** The Second Time *****************
"""
# Solution: if ([{ push to the stack and )]} pop
解法很巧妙， 入占和比较的都是')'.
最优解法
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        d = {'(':')','[':']','{':'}'}  # smart using of a dictionary
        stack = []
        for e in s:
            if e in d:
                stack.append(d[e])
            elif not stack or stack.pop()!= e:# not stack放前面因为stack是空的不能做pop()操作
                return False
        return not stack

"""
另一种写法
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')','{':'}','[':']'}
        stack = []
        for e in s:
            if e in d:
                stack.append(d[e])
            elif not stack or stack.pop()!=e:
                return False
        return stack == []

# ***************** The Third Time *********************
"""
My own soluiton:常规解法，成对就pop，代码繁琐
"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if s == []: return False
        stack = []
        for i in range(len(s)):

            if stack == [] or s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            if s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]==')' and stack[-1]!='(':
                stack.append(s[i])
            
            if s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif s[i]==']' and stack[-1]!='[':
                stack.append(s[i])
            
            if s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[i]=='}' and stack[-1]!='{':
                stack.append(s[i])
            
         
        return len(stack) == 0   # or return not stack







        


























