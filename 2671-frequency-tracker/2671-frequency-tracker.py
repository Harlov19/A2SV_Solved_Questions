class FrequencyTracker:

    def __init__(self):
        self.count_data = defaultdict(int)
        self.count_fequ = defaultdict(int)
       
    def add(self, number: int) -> None:
        self.count_fequ[self.count_data[number]]-=1
        self.count_data[number]+=1
        self.count_fequ[self.count_data[number]]+=1

    def deleteOne(self, number: int) -> None:
        if(self.count_data[number] == 0):
            return
        self.count_fequ[self.count_data[number]]-=1
        self.count_data[number]-=1
        self.count_fequ[self.count_data[number]]+=1
        

    def hasFrequency(self, frequency: int) -> bool:
        return  self.count_fequ[frequency]>0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)