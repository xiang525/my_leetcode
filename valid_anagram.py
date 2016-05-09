"""
O(nlogn) becaus sorted() function needs O(nlogn)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """       
        
        tmp = ''.join(sorted(s))
        if tmp == ''.join(sorted(t)):
            return True
        return False


"""
O(n), space O(n)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {};d2 = {}
        for e in s:
            if e not in d1:
                d1[e] = 1
            else:
                d1[e] += 1
        for e in t:
            if e not in d2:
                d2[e] = 1
            else:
                d2[e] += 1
        return d1 == d2