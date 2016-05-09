# 这道题应该是双指针s1,s2，从头扫描，每一步先移动s2，使s1-s2范围内包含答案，随后移动s1，
# 使包含结果的字符串最短.
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, S, T):
        count1={}; count2={}
        for char in T:
            if char not in count1: count1[char]=1
            else: count1[char]+=1
        for char in T:
            if char not in count2: count2[char]=1
            else: count2[char]+=1
        count=len(T)
        p1=0; minSize=100000; minStart=0
        for p2 in range(len(S)):
            if S[p2] in count2:  # match letters in T
                count1[S[p2]]-=1
                if count1[S[p2]]>=0: #避免match过的字符再被match
                    count-=1
            if count==0:  # T 中所有字符都已出现
                while True:
                    if S[p1] in count2 :
                        if count1[S[p1]] < 0:  #???
                            count1[S[p1]]+=1
                        else:
                            break
                    p1+=1
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        if minSize==100000: return ''
        else:
            return S[minStart:minStart+minSize]


"""
九章模板， 这样写代码更清晰
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        source = {};target= {}
        n = len(s); j = 0
        self.helper(target,t)
        ans = '';minLen = sys.maxint
        
        for i in range(n):
            while j < n and (self.isValid(source,target) == False):
                    if s[j] not in source:
                        source[s[j]] = 1
                    else:
                        source[s[j]] += 1
                    j += 1
                    
            if self.isValid(source,target):
                if minLen > j - i + 1:
                    minLen = j - i + 1
                    ans = s[i:j]
            source[s[i]] -= 1
        return ans
            
        
        
    def isValid(self,source,target):
        for i in target:
            if i not in source or target[i] > source[i]:
                return False
        return True
    
    def helper(self,d,strs):
        for e in strs:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1










