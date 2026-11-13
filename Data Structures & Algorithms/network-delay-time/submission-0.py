class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times: 
            adj[u].append((v,w))
        
        # create adjacency list
        # track distance at every visited node
        # update if distance is less
        # if reached every node then no infinity
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time): 
            # if visited already in a shorter time
            # then end the branch search
            if time >= dist[node]:
                return
            
            # update time in the case that less
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w) 

        
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1