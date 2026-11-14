class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # [1, 2, 2, 3, 3, 4, 4, 5]

        if len(hand) % groupSize != 0:
            return False
        
        numGroups = len(hand) // groupSize
        groups = [[] for _ in range(numGroups)]

        gi = 0
        r = 1

        sorted_hand = sorted(hand)
        groups[0].append(sorted_hand[0])

        # [[67],[67],[7],[7]]

        for i, v in enumerate(sorted_hand[1:]):
            if v == sorted_hand[i]:
                if gi + r >= len(groups):
                    return False
                
                groups[gi + r].append(v)
                r += 1
            else:
                while len(groups[gi]) == groupSize:
                    gi += 1

                if len(groups[gi]) > 0 and (v - groups[gi][-1]) != 1:
                    return False

                groups[gi].append(v)
                r = 1
            
        return True if len(groups[-1]) == groupSize else False
        
        # [1,1,2,2,3,3,4,4]
        # [[1,2,3,4], [1,2,3,4]]




              

