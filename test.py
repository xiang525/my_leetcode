class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        cnts = [0] * (N + 1)
        for c in citations:         
            cnts[[c, N][c > N]] += 1
      

        sums = 0
        for h in range(N, 0, -1):
            print h
            if sums + cnts[h] >= h:
                return h
            sums += cnts[h]
        return 0




if __name__ == '__main__':
    a = Solution()
    print a.hIndex([3, 0, 6, 1, 2,7])










