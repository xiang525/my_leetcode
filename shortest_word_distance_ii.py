"""
follow-up question对时间要求较高
O(m*n)
"""

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = collections.defaultdict(list)
        for index, val in enumerate(words):
            self.d[val].append(index)
        
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min([abs(index1-index2) for index1 in self.d[word1] for index2 in self.d[word2]])


"""
O(m+n)
"""
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = collections.defaultdict(list)
        for index, val in enumerate(words):
            self.d[val].append(index)
        
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i,j = 0,0; minLen = sys.maxint
        index1 = self.d[word1]; index2 = self.d[word2]
        while i < len(index1) and j < len(index2):
            minLen = min(minLen, abs(index1[i] - index2[j]))
            if index1[i] > index2[j]:
                j += 1
            else:
                i += 1
        return minLen





        