class DynamicArray:
    
    def __init__(self, capacity: int): # O(n) : n = capacity
        self.capacity = capacity
        self.size = 0 # 0 initially from getSize()
        self.arr = [0] * self.capacity



    def get(self, i: int) -> int: # O(1)
        return self.arr[i] 

    def set(self, i: int, n: int) -> None: # O(1)
        self.arr[i] = n


    def pushback(self, n: int) -> None: # O(1) - Avg case / Ammortized
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int: # O(1)
        # soft deletion
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None: # O(n)
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int: # num of values inserted into array / 0 initially | O(1)
        return self.size
            
    def getCapacity(self) -> int: # O(1)
        return self.capacity
