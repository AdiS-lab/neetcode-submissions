class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for con_node in adj[node]:
                if con_node not in visit:
                    visit.add(con_node)
                    dfs(con_node)

        res = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res += 1
        
        return res