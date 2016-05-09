class Solution(object):
    # in-place
    def reverseWords(self, s):
    # reverse the whole list
        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) -1:
                self.reverse(s, beg, i)
        print s
    
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1            


if __name__ == '__main__':
    a = Solution()
    a.reverseWords(["a b"])









