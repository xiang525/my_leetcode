"""此题估计是facebook面试题， 考查的是haystack结构
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    # 题意：实现字符串匹配函数，并返回一个指针，这个指针指向原字符串中第一次出现待匹配字符串的位置。
    # 如：haystack='aabbaa'; needle='bb'。如果使用python实现，则最后返回的应该是一个字符串，
    # 即：'bbaa'。
    def strStr(self, haystack, needle):

        if haystack == needle == '':
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i  +n] == needle:
                return i

        return -1


# ****************** The Second Time ************
"""
# Solution: Brute Force
# 题意：实现字符串匹配函数，并返回一个指针，这个指针指向原字符串中第一次出现待匹配字符串的位置。
# 如：haystack='aabbaa'; needle='bb'。如果使用python实现，则最后返回的应该是一个字符串，即：'bbaa'。
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if haystack == needle == '':
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:  # because of here counts to n thus the above line needs to substract n
                return i 
        return -1
                    















                    
