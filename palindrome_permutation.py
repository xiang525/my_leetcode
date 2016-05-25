"""
Leetcode的提示其实已经将答案告诉我们了。最笨的方法就是用Permutations的解法，找出所有的Permutation，
然后再用Palindrome中判断回文的方法来判断结果中是否有回文。但是我们考察一下回文的性质，
回文中除了中心对称点的字符，其他字符都会出现偶数次。而中心对称点如果是字符，该字符会是奇数次，
如果在两个字符之间，则所有字符都是出现偶数次。所以，我们只要判断下字符串中每个字符出现的次数，
就知道该字符串的其他排列方式中是否有回文了。
注意
本题也可以用一个HashSet，第偶数个字符可以抵消Set中的字符，最后判断Set的大小是否小于等于1就行了。
O(n) + O(n)
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for e in s:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        count = 0       
        for key in d:
            
            if d[key] % 2 != 0:
                count += 1
                if count > 1:
                    return False
        return True