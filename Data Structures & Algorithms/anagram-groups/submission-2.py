class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for i in range(len(strs)):
            sortStr = "".join(sorted(strs[i]))
            if sortStr in check: 
                check[sortStr].append(strs[i])
            else:
                check[sortStr] = [strs[i]];

        return list(check.values())
            


        