class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord,1)];
        count = 1
        #queue = collections.deque([(beginWord, 1)])
        wordlength = len(beginWord)
        #wordList.append(endWord)
        while queue:
            # count += 1
            # print 'count,queue: ',count,queue
            tmp = queue.pop(0)
            cur = tmp[0];length = tmp[1]
            if cur == endWord:return length
            for i in range(wordlength):
                part1 = cur[:i]; part2 = cur[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if cur[i]!=j:
                        nextWord = part1+j+part2
                        if nextWord in wordList:                            
                            queue.append((nextWord,length+1))
                            print 'queue: ',queue 
                            print nextWord,wordList,length                           
                            wordList.remove(nextWord)
                            
        return 0



if __name__ == '__main__':
    a = Solution()
    print a.ladderLength("hot","dog",["hot","dot","hog","dog"])







