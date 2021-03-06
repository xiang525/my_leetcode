class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
    	operands, operators = [],[]
    	operand = ""
    	for i in reversed(xrange(len(s))):
    		if s[i].isdigit():
    			operand += s[i]
    			if i == 0 or not s[i].isdigit():
    				operands.append(int(operand))
    				operand = ""
    		elif s[i] == ')' or s[i] == '*' or s[i] == '/':
				operators.append(s[i])
			elif s[i] == '+' or s[i] =='-':
				while operators and (operators[-1] == '*' or operators[-1]=='\'):
					self.compute(operands,operators)
					operators.append(s[i])
			elif s[i] == '(':
				while operators[-1]!=')':
					self.compute(operands,operators)
				operators.pop()

		while operators:
			self.compute(operands,operators)
		return operands[-1]

	def compute(self,operands,operators):
		left,right = operands.pop(),operands.pop()
		op = operators.pop()
		if op == '+':
			operands.append(left+right)
		elif op == '-':
			operands.append(left - right)
		elif op == '*':
			operands.append(left*right)
		elif op == '/':
			operands.append(left/right)



"""
test cases 过不去
"""
class Solution:
    # @param {string} s
    # @return {integer}
     def calculate(self, s):
        nums, ops = [], []
        operand = ""
        #for i in reversed(xrange(len(s))):
        for i in range(len(s)):
            if s[i].isdigit():
                operand += s[i]
                if i == len(s)-1 or not s[i+1].isdigit():
                    nums.append(int(operand))
                    print 'operand: ',operand
                    print 'nums: ',nums
                    operand = ""
            elif s[i] in '(*/':
                ops.append(s[i])
            elif s[i] in '+-':
                while ops and (ops[-1] in '*/'):
                    self.compute(nums, ops)
                ops.append(s[i])
            elif s[i] == ')':
                while ops[-1] != '(':
                    self.compute(nums, ops)
                ops.pop()
                
        while ops:
            self.compute(nums, ops)
        print nums    
        return nums[-1]

     def compute(self, operands, operators):
        right,left = operands.pop(), operands.pop()        
        op = operators.pop()
        print 'left,right,op:',left,right,op
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)
        
"""
论坛里的解法
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return "0"
        stack, num, sign = [], 0, "+"
        n = len(s)
        for i in xrange(n):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0") #处理多位数e.g., 10，78这种数                
            if (not s[i].isdigit() and not s[i].isspace()) or i == n-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp/num < 0 and tmp%num != 0: #处理-3/2 case, python里-3/2=2
                        stack.append(tmp/num+1)
                    else:
                        stack.append(tmp/num)
                sign = s[i]
                num = 0  #每次要清零
        return sum(stack)


"""
以下解法是有问题的
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return "0"
        stack, num, sign = [], 0, "+"
        n = len(s)
        for c in s:
            if c.isdigit():
                num = num*10+int(c)     
                print num, s.index(c), n
            if (not c.isdigit() and not c.isspace()) or s.index(c) == n-1:#c==0的index永远是1,因为多个一样的只会返回第一次出现的index
                print stack 
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp/num < 0 and tmp%num != 0:
                        stack.append(tmp/num+1)
                    else:
                        stack.append(tmp/num)
                sign = c
                num = 0 

        return sum(stack)
            

if __name__ == '__main__':
    a = Solution()
    print a.calculate("3+2*2")

