class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast_pointer = 0 
        slow_pointer = 0

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]] 
            if slow_pointer == fast_pointer:
                break

        # at this point, you are the x portion
        # slow_pointer and fast_pointer both point 
        # to the SAME INDEX - in this case i = 2

        slow_pointer_two = 0 
        while True:
            slow_pointer_two = nums[slow_pointer_two]
            slow_pointer = nums[slow_pointer]
            if slow_pointer == slow_pointer_two:
                return slow_pointer