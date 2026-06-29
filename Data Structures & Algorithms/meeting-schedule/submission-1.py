"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        seen = []
        for i in intervals:
            for j in seen:
                if i.start < j.end and i.start >= j.start or i.end > j.start and i.end <= j.end:
                    return False
            seen.append(i)
        return True