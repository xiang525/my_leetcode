"""
recursive solution, DP
"""
class Solution(object):
    def fibonacci_number(self,n):
        fp = [0]*n
        fp[0] = 1
        fp[1] = 1
        for i in range(2,n):
            fp[i] = fp[i-1] + fp[i-2]
        return fp


"""
recursive solution
"""
class Solution(object):
    def fibonacci_number(self,i):
        if i == 0: return 1
        if i == 1: return 1
        ans = self.fibonacci_number(i-1) + self.fibonacci_number(i-2)
        return ans

    def print_result(self,n):
        ans = []
        for i in range(n):
            ans.append(self.fibonacci_number(i))
        return ans

"""
non-recursive solution
"""
def fibonacci_number(self,n):
        if n <= 1:return 1
        fibo = 1
        fiboprev = 1
        for i in range(2,n):
            tmp = fibo
            fibo += fiboprev
            fiboprev = tmp
        return fibo 





