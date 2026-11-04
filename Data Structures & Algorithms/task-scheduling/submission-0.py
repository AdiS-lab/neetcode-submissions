class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # hash map of occurences
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque() # double ended queue

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time: # ordered where least is bottom
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


                