class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return Truet