class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # does num contain just positive? -> negative and positive and 0
        # is num sorted? -> no
        # can num be empty -> no
        # are any elements beyond float range -> no
        # so can I skip an element? -> no it must be contiguous

        # if all nums are negative can we just not sum at all? -> no your sum must have AT LEAST one element from nums -> subarray is non-empty

        # bruteforce
        # try out EVERY SINGLE possible subarray combination and find the one with largest sum

        # Input: nums = [2,-3,4,-2]
        # subarrays:

        # [2], [-3], [4], [-2]
        # [2,-3], [2,-4], [2,-2]
        # [-3, 4], [-3. -2]
        # [2,-3,4], [-3,4,-2]
        # [2,-3,4,-2]

        # for 2 you have 4 subarrays
        # for 3 you have 3 subarrays
        # for 4 you have 2
        # for -2 you have 1

        # 4 + 3 + 2 + 1 or n + n-1 + ... + 2 + 1 = n(n+1)/2
        # O(n^2) subarrays

        # time complexity = O(n^3) (since summing each subarray can cost up to O(n), for O(n^2) subarrays in total)


        # Optimal solution:

        # greedy
        # maximizing: sum
        # going through the array in order
        # is it better to have:
        # curr + sum so far 
        # or just starting fresh with curr

        # do keep track of max sum and the subarray that has the max

        # Input: nums = [2,-3,4,-2]

        # curr = 2, sum = 0 so go with curr + sum -> [2] -> max
        # curr = -3, so curr + sum = -3 + 2 = -1 so better - > [2, -3]
        # curr = 4 and curr + sum = 4 - 1 = 3 so better start fresh with curr -> [4] -> max
        # curr = -2 and curr + sum = -2 + 4 = 2 -> [4, -2]

        # so the max so far is [4] therefore we return the value

        # time = we start from the left -> worse case scenario is we go the whole array -> single pass -> O(n)
        # space = O(1) -> all you need is the max sum (we don't actually need the subarray)


        maxSum = nums[0]
        sumCurr = nums[0]
        curr = 0

        for i in range(1, len(nums)):
            curr = nums[i]
            if sumCurr + curr >= curr:
                sumCurr += curr
            else:
                sumCurr = curr
            maxSum = max(maxSum, sumCurr)
        

        return maxSum
            

 # Input: nums = [2,-3,4,-2]
 # maxSum = 2
 # sumCurr = 2
 # curr = 0

 # i = 1
 # curr = -3
 # sumCurr + curr = 2 -3 = -1
 # -1 > -3 so case 1
 # sumCurr = -1
 # maxsum = max(2, -1) = 2

 # i = 2
 # curr = 4
 # sumCurr + curr = -1 + 4 = 3
 # 3 < 4 so case 2
 # sumCurr = 4
 # maxsum = max(2, 4) = 4

 # i = 3
 # curr = -2
 # sumCurr + curr = 4 + -2 = 2
 # 2 > -2 so case 1
 # sumCurr = 2
 # maxsum = max(4, 2) = 4

 # end of loop
 # maxSum = 4





            



 

