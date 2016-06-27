class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s) #一定要先convert to a list 否则后面string不支持交换操作
        left = 0; right = n -1
        while left <= right:
            s[left], s[right] = s[right],s[left]
            left += 1; right -= 1
        return ''.join(s)