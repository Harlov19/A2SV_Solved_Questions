class Solution:
 def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list_1_dict = {}
        index_sum = {}
        min_index_sum = float('inf')
        for index,word in enumerate(list1):
            list_1_dict[word]=index
        for index,word in enumerate(list2):
            if(word in  list_1_dict):
                total = index + list_1_dict[word]
                index_sum[word]=   total
                min_index_sum = min(min_index_sum, total)
        return [word for word in index_sum if index_sum[word]==   min_index_sum]
        

