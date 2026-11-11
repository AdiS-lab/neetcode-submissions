class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj_list = {}

        for node1, node2  in edges:
            adj_list.setdefault(node1, []).append(node2)
            adj_list.setdefault(node2, []).append(node1)

        visiting = set()
        done = set()
        print(adj_list)

        def dfs(node, prev):
            if node in visiting:
                return True

            visiting.add(node)

            for next_node in adj_list[node]:
                if next_node == prev:
                    continue
                    
                if dfs(next_node, node):
                    return True

            done.add(node)
            visiting.remove(node)
            return False

        
        for key in adj_list.keys():
            if key not in done and dfs(key, -1):
                print(visiting)
                print("conditional is true")
                for v in reversed(edges):
                    print(v)
                    if v[0] in visiting and v[1] in visiting:
                        return [v[0], v[1]]
        
        return []

        
