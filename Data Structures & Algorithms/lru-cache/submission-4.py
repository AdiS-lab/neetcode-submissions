
# how to update the MRU in a way
# where order naturally moves MRU to the 
# left or right
# {3:4}
# some form of a queue, stack, or heap 
# but these don't support the idea of removing a specific value in rearranging
# hash map supporst removing and rearranging
# but doesn't support sorted order


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.storage = {}        
    # [2,6] [1,2]
    def get(self, key: int) -> int:
        if key in self.storage:
            temp_val = self.storage[key]
            del self.storage[key]
            self.storage[key] = temp_val
            return temp_val

        return -1
        
    def put(self, key: int, value: int) -> None:
        # if get val then delete + insert again 
        # this moves to last in insertion order
        # pop the first (or LRU)
        
        if key in self.storage:
            del self.storage[key]
        elif self.length == self.capacity:
            self.storage.pop(next(iter(self.storage)))
        else:
            self.length += 1

        self.storage[key] = value

# {1:10, 2:20}
        
