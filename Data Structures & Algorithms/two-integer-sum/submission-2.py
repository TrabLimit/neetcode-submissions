class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        last_index = len(nums)
        print(last_index)

        for index, num in enumerate(nums):
            remainder = target - nums[index]
            print(remainder)

            nums_left = nums[index + 1 : last_index]
            
            if remainder in nums_left:
                return [index, nums_left.index(remainder) + index + 1]