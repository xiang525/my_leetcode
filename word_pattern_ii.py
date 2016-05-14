"""
跟word pattern 那题很像但是没有空格能够区分对应关系，所以要用dfs recurively找到pattern中对应的
str。此题用一个字典就可以解决, 如果要进一步提高查找速度的话可以用两个字典
"""
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.helper(pattern, str, 0, 0, {})
 
     
    def helper(self, pattern, str, i, j, d1):
        if i == len(pattern) and j == len(str):
            return True
        elif i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in d1:
                w = d1[p]
                if w == str[j:j+len(w)]:
                    if self.helper(pattern, str, i + 1, j + len(w), d1):
                        return True
            else:
                for k in range(j, len(str)):
                    w = str[j:k+1]
                    if w not in d1.values():
                        d1[p] = w
                        if self.helper(pattern, str, i + 1, k + 1, d1):
                            return True
                        d1.pop(p)
        return False