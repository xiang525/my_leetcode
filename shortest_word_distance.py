"""
O(n) + O(1) space
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(words); index1, index2 = n,n
        minLen = sys.maxint
        for i in range(n):
            if words[i] == word1:
                index1 = i
                minLen = min(minLen,abs(index1 - index2))
            if words[i] == word2:
                index2 = i
                minLen = min(minLen,abs(index1 - index2))
        return minLen