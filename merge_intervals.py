# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
    	intervals.sort(key=lambda x:x.start)
    	length = len(intervals)
    	res = []
    	for i in range(length):
    		if res == []:
    			res.append(intervals[i])
    		else:
    			size = len(res)
    			if res[size-1].start <= intervals[i].start<= res[size-1].end:
    				res[size-1].end = max(intervals[i].end, res[size-1].end)
    			else:
    				res.append(intervals[i])
    	return res


#  ****** The Second Time ********
# 解题思路：先将区间按照每个start的值来排序，排好序以后判断一个区间的start值是否处在前一个区间中，
# 如果在前一个区间中，那么合并；如果不在，就将新区间添加。
# 一开始忘记要排序了；网上做法是朝前看,貌似我的往后看不work

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        res = []
        for i in range(n):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start<= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res
        
 # 以下是往后看， 不work

    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        res = []
        for i in range(n-1):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if intervals[i].start<= res[size-1].end<= intervals.end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res








            






















