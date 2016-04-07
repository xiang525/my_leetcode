# A better describtion of the question: http://www.careercup.com/question?id=4425679

class Solution:
    # @param {integer} n
    # @return {string}
    def count(self,s):
    	cur = '#';count = 0; t= ''
    	for i in s:
    		if i!=cur:
    			if cur!='#':
    				t+=str(count)+cur
    			cur = i
    			count = 1
    		else:
    			count+=1
    	t+=str(count)+cur
    	return t
        
    def countAndSay(self, n):
    	s = '1'
    	for i in range(2,n+1):
    		s = self.count(s)
    	return s


    	
"""
# Solution: two pointers, prev and cur
"""


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
    	s = '1'
    	for i in range(0,n-1):
    		prev = newS = ''
    		num = 0
    		for cur in s:
    			if prev!='' and prev!=cur:
    				newS+=str(num)+ prev
    				num = 1
    			else:
    				num+=1
    			prev = cur
    		newS += str(num)+prev
    		s = newS
    	return s









