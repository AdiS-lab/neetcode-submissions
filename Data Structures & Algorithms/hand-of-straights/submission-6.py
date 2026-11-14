class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False


        count = Counter(hand) # frequency of each value
        hand.sort()

        # [1,3,5,7]

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize): # consecutive building
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True
        