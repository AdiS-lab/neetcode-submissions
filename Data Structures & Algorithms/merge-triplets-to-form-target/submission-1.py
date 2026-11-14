class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # operation = find max between two triplets 
        # try to obtain the target doing that operation multiple times

        # merging iff the resulting maxes are less than or oequal to the respecitive target
        

        curr = triplets[0]

        for v in triplets[1:]:
            first = max(v[0], curr[0]) 
            second = max(v[1], curr[1])  
            third = max(v[2], curr[2]) 

            if first <= target[0] and second <= target[1] and third <= target[2]:
                curr = [first, second, third]
            
            if curr[0] > target[0] or curr[1] > target[1] or curr[2] > target[2]:
                curr = [v[0], v[1], v[2]]
        
        return True if curr == target else False
        