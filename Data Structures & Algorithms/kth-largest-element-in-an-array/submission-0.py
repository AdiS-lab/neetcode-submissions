class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-n for n in nums]
        heapq.heapify(heap)
        
        val = 0
        for _ in range(k):
            val = heapq.heappop(heap)

        return -val
        # heappify will turn existing arr into a heap 
        # can pop the largest   
        