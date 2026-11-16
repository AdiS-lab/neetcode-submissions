class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals 
        
        sorted_intervals = sorted(intervals, key = lambda x:x[0] )
        res = [sorted_intervals[0]]

        for s, e in sorted_intervals[1:]:
            end = res[-1][1]
            start = res[-1][0]

            if s <= end:
                res[-1] = [start, max(e, end)]
            
            if s > end and e > end:
                res.append([s, e])

        return res
        