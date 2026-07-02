class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Attempt 2: Exploit the fact that set cannot have duplicates
        
        nums_set = set(nums) # Convert to set (it will remove duplicates)
        if (len(nums) != len(nums_set)):
            return True
        return False

        
        # Attempt 1: inefficient

        #for index, element in enumerate(nums):
        #    chosen_element = nums.pop(index)
        #    if chosen_element in nums:
        #        return True
        #    nums.insert(index, chosen_element)
        #return False




        


        