"""
not the best solution
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tmp = 0
            while num > 0:
               tmp += num%10
               num /= 10
            num = tmp
        return num


"""
https://en.wikipedia.org/wiki/Digital_root
digital root formula
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num-1) % 9 + 1