class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if h = length, k = max(piles)
        # moves = len(piles) - h 
        # first thought is to find maximum and increment from there
        # any attempt at finding minimum directly can result in arbitrary values
        # some type of sort probably necessary\
        
        min_guess = 1 
        max_guess = max(piles)

        if sum(piles) <= h: # k = 1
            return min_guess
         
        if len(piles) == h: # k = max(arr)
            return max_guess

        final_val = -1

        while min_guess < max_guess:

            mid_guess = (min_guess + max_guess) // 2
            
            hours = 0
            for i in range(len(piles)):
                if min_guess >= piles[i]:
                    hours += 1
                else:
                    hours += math.ceil(piles[i] / mid_guess)
            


            if hours <= h:
                final_val = mid_guess
                max_guess = mid_guess
            else:
                min_guess = mid_guess + 1

        return final_val


        