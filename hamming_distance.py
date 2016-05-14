"""
Houzz面经里出现过但leetcode里没有
Calculate the distance of bits between two integers. 
For example: 1 -> 01; 2 -> 10; dist = 2
wiki: https://en.wikipedia.org/wiki/Hamming_distance
"""
def hamming_distance(x,y):
	distance = 0
	val = x^y  #异或就知道有多少位不同
	while val!= 0:
		distance += 1
		val &= val - 1
	return distance

"""
类似与number of 1-bit的解法
"""
def hamming_distance(x,y):
	distance = 0
	val = x^y
	while val!= 0:
		distance += val & 1
		val >>= 1
	return distance