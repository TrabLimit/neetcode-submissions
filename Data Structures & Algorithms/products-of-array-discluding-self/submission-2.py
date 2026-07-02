class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        product = math.prod(nums)

        for number in nums:
            quotient = 0
            if number == 0: # watch out, we cannot divide by 0
                nums_copy = nums[:] # make a copy
                nums_copy.remove(number)
                quotient = math.prod(nums_copy)
            else:
                quotient = product // number
            result.append(quotient)

        return result
        