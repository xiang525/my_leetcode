class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
    	return ' '.join([item for item in reversed(s.split(' ')) if item])


"""
My own solution:用了O(n)space不是最优解
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):        
        a = s.split(" ")    
        b = []
        for i in a:
            if i != "":
                b.insert(0,i)      
        return ' '.join(b)

"""
最优解
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):  
        return ' '.join(s.split()[::-1])

"""
九章的三步反转法
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:return ''
        tmp = s.split()
        return ' '.join(self.reverse(tmp,0,len(tmp)-1))        
        
    def reverse(self,s,begin,end):
        while begin < end:
            s[begin],s[end] = s[end],s[begin]
            begin += 1
            end -= 1
        return s
