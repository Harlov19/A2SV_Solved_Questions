class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.num_map = {}

    def insert(self, val: int) -> bool:
        if(val not in self.num_map):
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if(val not in  self.num_map):
            return False
        index = self.num_map[val]
        last = self.num_list[-1]
        self.num_list[index] = last
        self.num_list.pop()
        self.num_map[last] = index
        del self.num_map[val] 
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()