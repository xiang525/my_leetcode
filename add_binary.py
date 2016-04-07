class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
    	a = int(a,2)
    	b = int(b,2)
    	return bin(a+b)[2:]  # 0b means binary so we need to read from the 3rd one


####
  # ************ The Second Time ***************
  """
  想想十进制是如何转二进制的， 就是除以2得余数 %
  """
  class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        solution = []
        sum = 0
        for i in range(0,max(len(a),len(b))):
            if i < len(a) and a[len(a)-1-i]=='1':
                sum += 1
            if i < len(b) and b[len(b)-1-i]=='1':
                sum += 1
            solution.insert(0,str(sum%2))  # % 后往前插
            sum /= 2
        if sum > 0:
            solution.insert(0,str(sum%2))
        return ''.join(solution)
