"""
比较恶心的一道题，没有明确给出定义，给了一些例子，需要自己不断去尝试。首先要把前后的空字符给去掉。
然后依次考虑符号、数字、小数点、数字，如果有这些中连续的几个，表示目前是一个普通的数值。继续判断"e"
（注意大小写都可以），接着判断符号、数字，如果e后面没有数字，那么这是一个不正常的科学类数值。
最后根据三种情况来综合判断，要满足目标是一个数值类型，那么首先要保证e前面的数是正常的，如果有e的话，
要保证它后面的数也是正常的，最后要保证整个字符串都已经遍历玩了，如果没有说明中间出现了一些异常的字符或
者末尾多了一些多余的字符。
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        length = len(s)
        i = 0
        # Deal with symbol
        if i < length and (s[i] == '+' or s[i] == '-'):
            i += 1
        is_normal = False
        is_exp = True
        # Deal with digits in the front
        while i < length and s[i].isdigit():
            is_normal = True
            i += 1
        # Deal with dot ant digits behind it
        if i < length and s[i] == '.':
            i += 1
            while i < length and s[i].isdigit():
                is_normal = True
                i += 1
        # Deal with 'e' and number behind it
        if is_normal and i < length and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            is_exp = False
            if i < length and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < length and s[i].isdigit():
                i += 1
                is_exp = True
        # Return true only deal with all the characters and the part in front of and behind 'e' are all ok
        return is_normal and is_exp and i == length


"""
另一种写法
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        n = len(s)
        i = 0
        if i < n and s[i] in '+-':
            i += 1
        is_normal = False
        is_exp = True
        while i < n and s[i].isdigit():
            is_normal = True
            i += 1
        if i < n and s[i]=='.':
            i+= 1
            while i < n and s[i].isdigit():
                is_normal = True
                i += 1
        if is_normal and i < n and s[i] in 'eE':
            i += 1
            is_exp = False
            if i < n and s[i] in '+-':
                i += 1
            while i < n and s[i].isdigit():
                i += 1
                is_exp = True
        return is_normal and is_exp and i == n









