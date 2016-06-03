"""
论坛里的写法非常简洁
此题没有算法难道但是要bug free不容易
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:                
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' ' #题目要求左边加的空格较多, 最右边不加空格                   
                res.append(''.join(cur))
                cur, num_of_letters = [], 0 #清零为下一行做准备
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)] #左对齐输出（对最后一行的处理）

    		
    		
    		