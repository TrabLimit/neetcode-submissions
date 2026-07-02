class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        last_index = len(nums) # get the final index
        # print(last_index)

        for index, num in enumerate(nums):
            # since there's only 2 numbers adding, we can get the remainder of sum
            remainder = target - nums[index] 
            print(remainder)

            # and search from the remaining list (think of it as looping from j = i+1)
            nums_left = nums[index + 1 : last_index]
            
            if remainder in nums_left:
                return [index, nums_left.index(remainder) + index + 1] 
                # make sure to get the index from the leftover list