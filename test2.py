class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s)
        left = 0; right = n -1
        while left <= right:
            print s[left], s[right]
            s[left], s[right] = s[right],s[left]
            left += 1; right -= 1
        return ''.join(s)
        


if __name__ == "__main__":
    a = Solution()
    print a.reverseString("hello")
    












