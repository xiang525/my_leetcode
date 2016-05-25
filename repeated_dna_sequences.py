class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):

    	d = {}
    	res = []
    	for i in range(len(s)):
    		key = s[i:i+10]
    		if key not in d:
    			d[key] = 1
    		else:
    			d[key] += 1

    	for e in d:
    		if d[e] > 1:
    			res.append(e)

    	return res



class Solution:
    # @param {string} s
    # @return {string[]} 


    def findRepeatedDnaSequences(self, s):
        d = {}
        ans = []
        for i in range(len(s)):
            if i + 10 <= len(s):  # I think we need this judegment. This is from my own part.
                part2 = s[i:i+10]
                tmp =  part2
                if tmp not in d:
                    d[tmp] = 1
                else:
                    d[tmp]+=1
        for key in d:
            if d[key] > 1:
                ans.append(key)
        return ans


"""
The second programing way
以下解法超烂
"""
class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        d = {}; n = len(s);ans = []
        if n < 10:return ans
        for i in range(n):
            key = s[i:i+10]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
                if key not in ans:
                    ans.append(key)
        return ans


"""
论坛里的写法
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = collections.defaultdict(int) # int!!
        for i in range(len(s)):
            d[s[i:i+10]] += 1
        return [key for key,val in d.iteritems() if val > 1]














