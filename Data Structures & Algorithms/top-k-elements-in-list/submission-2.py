class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map to store frequencies and sort by the top 2
        

        if not nums:
            return []
        
        seen = {}
        for v in nums:
            seen[v] = seen.get(v, 0) + 1

        top = sorted(seen.items(), key=lambda x: -x[1])[:k]
        
        return [k for k, v in top]
         