"""
论坛里的解法O(n), 没有用到字典
"""
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words or len(words) < 2: return -1
        p1 = -1; p2 = -1; minLen = sys.maxint
        
        for i in range(len(words)):
            if words[i] == word1 and word1 != word2:
                p1 = i
            if words[i] == word2
                if word1 == word2:
                    p1 = p2 # p1总是等于上一个p2的值
                p2 = i
            if p1 != -1 and p2 != -1:
                minLen = min(minLen, abs(p2 - p1))
        return minLen