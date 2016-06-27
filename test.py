
import heapq
class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def firstN(self, strs, n):
        heap = []
        tmp = strs.split(); d = collections.defaultdict(list)
        ans = []; freq = {}

        
        for e in tmp:
            if e not in freq:
                freq[e] = 1
            else:
                freq[e] += 1

        for index, value in enumerate(freq):
            d[].append()



        for key in freq:            
            heapq.heappush(heap,-freq[key])             
            

        for i in range(n):
            pop = -1*heapq.heappop(heap)


        return ans




        






if __name__ == '__main__':
    ins = Solution()
    a = "a a b b c c beta beta beta alpha"
    print ins.firstN(a,2)
    
    