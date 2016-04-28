"""
# 解题思路：这道题使用bfs来解决。使用BFS, 单词和length一块记录, dict中每个单词只能用一次, 所以用过即删。
# dict给的是set类型, 检查一个单词在不在其中(word in dict)为O(1)时间。设单词长度为L, dict里有N个单词, 
# 每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母, 
# 看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。
此题很有意思，用了小技巧
"""


class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
    	wordDict.add(endWord)
    	q = []
    	q.append((beginWord,1)) # 记录单词的同时也记录长度
    	while q:
    		curr = q.pop(0)
    		currword = curr[0]; currlen = curr[1]
    		if currword == endWord: return currlen
    		for i in range(len(beginWord)):
    			part1 = currword[:i]; part2 = currword[i+1:] # part 1中currwrod[i]是取不到的
    			for j in 'abcdefghijklmnopqrstuvwxyz':
    				if currword[i] != j:
    					nextword = part1 + j + part2
    					if nextword in wordDict:
    						q.append((nextword,currlen+1))
    						wordDict.remove(nextword)  #不移去已经出现的词会再次出现不满足题意
    	return 0




        wordList.add(endWord)
        q = []
        q.append((beginWord,1))
        while q:            
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == endWord:return currlen
            for i in range(len(beginWord)):
                part1 = currword[:i];part2 = currword[i+1:]
                for j in 'abcdefghijkmnopqrstuvwxyz':
                    if currword[i]!= j:
                        nextword = part1+j+part2                        
                        if nextword in wordList:
                            q.append((nextword,currlen+1))
                            wordList.remove(nextword)
                           
        return 0

"""
my own Solution
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord,1)];
        wordlength = len(beginWord)        
        while queue:
            tmp = queue.pop(0)
            cur = tmp[0];length = tmp[1] # length 不能设为全局变量
            if cur == endWord:return length
            for i in range(wordlength):
                part1 = cur[:i]; part2 = cur[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if cur[i]!=j:
                        nextWord = part1+j+part2
                        if nextWord in wordList:                            
                            queue.append((nextWord,length+1))
                            wordList.remove(nextWord)
        return 0

"""
以下是常见的错误解法:这种解法length不是最短应为当一步有多种选择时length被多次加1，我想了很久才弄明白
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [beginWord];
        length = 1
        wordlength = len(beginWord)
        
        while queue:
            tmp = queue.pop(0)
            cur = tmp[0];length = tmp[1]
            if cur == endWord:return length
            for i in range(wordlength):
                part1 = cur[:i]; part2 = cur[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if cur[i]!=j:
                        nextWord = part1+j+part2
                        if nextWord in wordList:                            
                            queue.append(nextWord)
                            wordList.remove(nextWord)
            length += 1
        return 0


