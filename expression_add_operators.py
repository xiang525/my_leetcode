"""
需要记录last oprand，为的是处理乘号的情况。乘号时的计算公式为: result - lastOP + lastOP * curVaule，
如 2 + 3 * 5, 当计算到要乘5时，result = 2 + 3 = 5, lastOp = 3, curValue = 5, 
则最终结果为： 5 - 3 + 3 * 5 = 17 = 2 + 3 * 5。
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
    
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)


"""
另一种写法
"""
class Solution(object):
   
    def addOperators(self, num, target):  
        """ 
        :type num: str 
        :type target: int 
        :rtype: List[str] 
        """  
        def dfs(num, lastOp, result, value):  
            if len(num) == 0:  
                if target == result:  
                    ans.append(value)  
                return
            for i in range(1, len(num) + 1):  
                cur = num[:i]  
                if len(cur) > 1 and cur[0] == "0":  
                    continue  
                if len(value) == 0: 
                    dfs(num[i:], int(cur), int(cur), value + cur)  
                else:  
                    dfs(num[i:], int(cur), result + int(cur), value + "+" + cur)  
                    dfs(num[i:], -int(cur), result - int(cur), value + "-" + cur)  
                    dfs(num[i:], lastOp * int(cur), result - lastOp + lastOp * int(cur), value + "*" + cur)  
            
        ans = []  
        dfs(num, 0, 0, "")  
        return ans  