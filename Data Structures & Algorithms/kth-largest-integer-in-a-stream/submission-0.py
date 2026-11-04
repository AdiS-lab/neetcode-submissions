class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums)[-self.k]

# sort as it is coming in
# second largest = sorted[]