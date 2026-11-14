class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c in enumerate(s)}

        res = []
        end = 0
        start = 0
        
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(i - start + 1) 
                start = i + 1
        return res 