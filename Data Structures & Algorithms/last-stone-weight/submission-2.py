class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # heap is akin to a binary tree where smallest node is at top
        # O(logn) for heappush or heappop

        # smallest value, is biggest abs

        heap = [-s for s in stones] # turns to negatives values
        heapq.heapify(heap) # O(n)

        while len(heap) > 1:
            y = -heapq.heappop(heap) # negative to revert
            x = -heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y-x))
        
        return -heap[0] if heap else 0


