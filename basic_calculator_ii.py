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
        

            

if __name__ == '__main__':
    a = Solution()
    print a.calculate("3+2*2")

