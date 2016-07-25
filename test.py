class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s,l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return l+1, r
            
        res = ''
        for i in range(len(s)):
            
            start, end = helper(s,i,i)
            print start, end
            if end-start > len(res):
                res = s[start: end-1]
            start, end = helper(s, i, i+1)
            if end-start > len(res):
                res = s[start, end]
        return res







if __name__ == '__main__':
    ins = Solution()
    ins.longestPalindrome("a")
    
    