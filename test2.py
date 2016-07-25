class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):  
        s = s.split()        
        for i in xrange(len(s)):
            s[i] = s[i][::-1]            
        return ' '.join(s)



        


if __name__ == "__main__":
    a = Solution()
    strs = 'this is a great company'
    print a.reverseWords(strs)
    












