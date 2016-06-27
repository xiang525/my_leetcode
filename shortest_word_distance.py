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
                minLen = min(minLen,abs(index1 - index2))#注意不要讲这一句写在循环外面因为当i都不等于时不需要update minDistance的value
            if words[i] == word2:
                index2 = i
                minLen = min(minLen,abs(index1 - index2))
        return minLen