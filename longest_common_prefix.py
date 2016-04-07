# this is a good solution. The codes are clean.

class Solution:
    # @param {string[]} strs
    # @return {string}
    def get_common_prefix(self, x, y):
      LCP_length = 0

      for i in range(0, min(len(x), len(y))):
        if x[i] != y[i]:
          break

        LCP_length += 1

      return x[:LCP_length]


  # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        return reduce(self.get_common_prefix, strs) # by order any two of strings in strs will call
        # self.get_common_prefix each time. 




# ******************** The Second Time *******************
# 解题思路：找出所有字符串共同的前缀。strs have many strings not one
# This is not the best solution
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	n = len(strs)
    	if n==0:
    		return ''
    	if n==1:
    		return strs[0]
    	prefix = list(strs[0])
    	for str in strs[1:]:
    		if len(prefix) < len(str):
    			length = len(prefix)
    		else:
    			length = prefix[:len(str)]
    		if length == 1:
    			if prefix[0] == str[0]:
    				prefix = prefix[0]
    			else:
    				prefix = []
    		else:
    			for i in range(length):
    				if prefix[i] != str[i]:
    					prefix = prefix[:i]
    					break
    	return ''.join(prefix)


"""
Solution 3: common prefix有的话必然存在于每一个string里面， 利用这一点来解题
"""
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0: return ''
        if n == 1: return strs[0]
        length = [len(i) for i in strs]
        common_prefix = ''

        for i in range(min(length)):
            tmp = strs[0][i]
            for j in xrange(1,n):
                if strs[j][i] != tmp:
                    return common_prefix
            common_prefix += tmp
        return common_prefix









if __name__ == '__main__':
	a = Solution()
	strs = 'hello'
	print a.longestCommonPrefix(strs)