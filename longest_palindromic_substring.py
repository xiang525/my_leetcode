class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        max_s = ''
        for i in xrange(len(s)):
            s1 = self.extend(s, i)
            if len(s1) > len(max_s):
                max_s = s1
            s2 = self.extend(s, i, i+1)
            if len(s2) > len(max_s):
                max_s = s2
        return max_s
 
    def extend(self, s, i, j=None):
        if j:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i+1:j]
        else:
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j, k = j - 1, k + 1
            return s[j+1:k]
    	


"""
O(n*n)。对于每一个字符，以之作为中间元素往左右寻找。注意处理奇偶两种模式：
1. aba
2. abba
space is O(n)不是最优解
"""
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]


"""
最优解 run time O(n^2)
space O(1)
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s,l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return l+1, r
            
        res = ''
        for i in range(len(s)):
            start, end = helper(s,i,i)
            if end-start > len(res):
                res = s[start: end]
            start, end = helper(s, i, i+1)
            if end-start > len(res):
                res = s[start: end]
        return res




    
