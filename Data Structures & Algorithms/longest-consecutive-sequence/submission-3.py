class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        # remove duplicates & sort -> makes our job easier
        nums = sorted(list(set(nums)))
        print(nums)

        max_count = 1
        curr_count = 1

        if len(nums) == 1:
            return 1

        i = 0;
        while i < len(nums)-1:
            # print(nums[i])

            if nums[i+1] == nums[i] + 1: # if consecutive, increment
                curr_count += 1
            else: # otherwise reset to 1
                curr_count = 1

            if curr_count > max_count: # update max_count
                max_count = curr_count
            
            i += 1
        
        return max_count



