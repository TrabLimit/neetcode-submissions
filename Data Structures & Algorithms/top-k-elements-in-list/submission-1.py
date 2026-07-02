class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {} # make empty dictionary!

        for num in nums:
            if num in count_dict: # if it's already there!
                count_dict[num] += 1;
            else:
                count_dict[num] = 1;
        
        print(count_dict)

        # sort by frequency    
        sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
        # reverse the sort so high -> low order is given
        
        print(sorted_dict)

        keys_list = list(sorted_dict) # this is what we need
        values_list = list(sorted_dict.values()) # not needed, but made one so you know how to extract values

        return keys_list[:k]
        