class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s); n = len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1 or s == t: #把小的放前面这样后面的for循环用m
            return False
        for i in range(m):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True