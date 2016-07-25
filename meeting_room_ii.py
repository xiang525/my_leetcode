class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        numRoom = available = 0
        i = 0
        for start in starts:
            while ends[i] <= start:
                available += 1
                i += 1
            if available:
                available -= 1
            else:
                numRoom += 1
        return numRoom