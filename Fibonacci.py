"""
O(2^n) recursive
"""

def fibonacci(n):
	if n == 0: return 0
	elif n == 1: return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

"""
iterative
"""
def fibonacci(n):
	a, b = 0, 1
	for i in range(1,n):
		a, b = b, a+b
	return b