class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [[1,0],[2,1]
        # [[1,2], [2,3]]

        # can go from 2 --> 1 
        # then after 3 --> 2

        # it only goes before and after
        # if in done then has to be a prequisite to an existing list
        # global arr and prepend and append depending on the state

        # one solution to get all ordered values is just return node
        # and append each dfs to said node

        # init all prequisites
        preq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preq[crs].append(pre)


        visit, cycle = set(), set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True

            cycle.add(node)

            for v in preq[node]:
                if dfs(v) == False:
                    return False
            
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for c in preq:
            if dfs(c) == False:
                return []
        return res
        

        

            
        


