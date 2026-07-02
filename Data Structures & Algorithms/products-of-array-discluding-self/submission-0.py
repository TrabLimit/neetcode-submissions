class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        product = math.prod(nums)

        for number in nums:
            quotient = 0
            if number == 0:
                temps_nums = nums[:]
                temps_nums.remove(number)
                quotient = math.prod(temps_nums)
            else:
                quotient = product // number
            result.append(quotient)

        return result
        