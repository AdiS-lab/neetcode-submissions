class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if not s:
            return []

        res = []                 
          
        def dfs(pal, i):
            if i == len(s):
                if pal[-1][::-1] == pal[-1]:
                    res.append(pal.copy())
                return

            if pal[-1][::-1] == pal[-1]:
                pal.append(s[i])
                dfs(pal, i + 1)
                pal.pop()
            

            pal[-1] = f"{pal[-1]}{s[i]}"
            dfs(pal, i + 1)

            return

        dfs([s[0]], 1)

        return res
