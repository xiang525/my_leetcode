"""
解法与Isomorphic Strings （205） 一样
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        cur = str.split()
        d = {};n = len(pattern); m = len(cur)
        if n != m:return False
        for i in range(n):
            if pattern[i] not in d:
                if cur[i] not in d.values():
                    d[pattern[i]] = cur[i]
                else:
                    return False
            else:
                if d[pattern[i]] != cur[i]:
                    return False
                    break
        return True