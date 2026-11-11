class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {c: [] for c in range(numCourses)}

        for course, preq in prerequisites:
            adj_list[preq].append(course)

        visiting, done = set(), set()
        def dfs(course):
            if course in visiting:
                return False
            if course in done: 
                return True

            visiting.add(course)

            for r in adj_list[course]:
                if dfs(r) == False:
                    return False
            
            visiting.remove(course)
            done.add(course)
            return True
        
        for k in adj_list.keys():
            if not dfs(k):
                return False
        return True
