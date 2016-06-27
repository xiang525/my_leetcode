"""
其实arrays 是2D的， 所以肯定要记录二维坐标 i, j; i用来确定是哪一个list, j 用来确定每一个list里面
"""
import heapq

class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))# index 就是i， 0就是j
             
        while heap:       
            
            tmp = heapq.heappop(heap)            
            val = tmp[0]; x = tmp[1]; y = tmp[2]
            result.append(val)
            if y + 1 < len(arrays[x]):#y+1用来判断下一个元素                
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))            
        return result


if __name__ == '__main__':
    ins = Solution()
    a = [1,8,9,12]
    b = [3,4,19,22,23]
    c = [2,3,6,20,21,33,45]
    arrays = [a,b,c,]
    print ins.mergekSortedArrays(arrays)