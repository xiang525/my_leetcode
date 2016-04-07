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


