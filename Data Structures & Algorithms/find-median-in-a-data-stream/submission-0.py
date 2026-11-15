# first idea is to sort and then if even

class MedianFinder:

    def __init__(self):
        self.storage = []
        

    def addNum(self, num: int) -> None:
        self.storage.append(num)
        
    def findMedian(self) -> float:
        self.storage.sort()
        length = len(self.storage)

        if length % 2 == 0:
            ind_one = (length // 2) - 1 # 1
            ind_two = length // 2 # 2

            return (self.storage[ind_one] + self.storage[ind_two])/2
        else:
            return self.storage[length//2] 

        