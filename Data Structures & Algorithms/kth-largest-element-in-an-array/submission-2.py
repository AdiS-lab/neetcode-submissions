class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # idea is always push, once greater than k, then 
        # pop smallest, this way nth largest value will be at 0 

        heap = []
        for v in nums: 
            heapq.heappush(heap,v)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]