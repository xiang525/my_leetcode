class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        t = ''.join(s).split(' ')
        
        s[:] = list(' '.join(reversed(t)))