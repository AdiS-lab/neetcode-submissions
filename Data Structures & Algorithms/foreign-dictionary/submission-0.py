class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        # key is less than value lexicographically
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""

            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        visited = {}
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])


'''

first letter where differ means that that letter is smaller

words = ["hrn","hrf","er","enn","rfnn"]

n < f

words = ["hrn","hrf", "enj", "efj"]

invalid is when compared letters 
don't match later down the road

if second word ever terminates before first word = invalid
if second letter difference is already in hash map  = invalid
return from 


'''