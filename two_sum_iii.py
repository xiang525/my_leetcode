"""
论坛里的解法，不用字典会超时
value - num != num 专门处理value = 0, num = 0 (only one '0')这种情况
"""
class TwoSum(object):

    def __init__(self):
        self.ctr = {}

    def add(self, number):
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False