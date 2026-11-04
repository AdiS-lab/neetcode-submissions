class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for v in points:
            x1, y1 = v[0], v[1]
            distance = math.sqrt(x1**2 + y1**2)
            heapq.heappush(heap, (-distance, x1, y1))
            if len(heap) > k:
                heapq.heappop(heap) # pops the SMALLEST value, or the BIGGEST abs distance
        
        return [(x,y) for _, x, y, in heap]