"""
论坛里的解法
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mp = {w:i for i, w in enumerate(words)}
        ret = []
        for i, w in enumerate(words):
            for j in xrange(len(w) + 1):
                a = w[:j]
                b = w[j:]                
                if a == a[::-1]:
                    if mp.has_key(b[::-1]) and mp[b[::-1]] != i:
                        ret.append((mp[b[::-1]], i))

                if b == b[::-1]:
                    if mp.has_key(a[::-1]) and mp[a[::-1]] != i:
                        ret.append((i, mp[a[::-1]]))

        return list(set(ret))