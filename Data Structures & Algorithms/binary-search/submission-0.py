class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # nums is distinct integers (pos and neg and 0)
        # nums is sorted lowest -> highest
        # nums has AT LEAST one elemnt
        # target is integer

        # we return the INDEX of the target, if found
        # otherwise -1

        # sample test case:
        # nums = [-2, 0, 2, 3, 4], tar = 2
        # output: 2 

        # nums = [0], tar = 1
        # output: -1

        # nums = [0, 10, 20], tar = 5
        # output: -1


        # bruteforce:
        # we iterate EVERY element from either left or right
        # for each iteration check if that element matches the target
        # if so, we return the index (or the interation number)
        # otherwise we would be going through the whole array, not finding the target, thus returning -1

        # time complexity = O(n) (iterating every element, comparing is constant)
        # space complexity = O(1) (no additonal data structure needed: current element to which we'lll compare it against target)


        # optimal solution:
        # we can try binary search
        # termination: if the num is empty return -1 (couldn't not find target)
        # 1. We determine the mid-index (save the value)
        # 2. compare the mid index element with the target 
        #       if target = num[mid] return mid
        #       if target > num[mid] return iteration with the right half of num (mid+1 ... end )
        #       else return iteration with the left half of num (start ... mid-1)

        # time complexity = continuous division by factor of 2 n = 2^k, k = log_2 n (k is number of iteraitons) -> O(logn)
        # space complexity = O(1) (no addional data structure required)



        left = 0

        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1 # left half
            else:
                left = mid + 1 # right half
        
        return -1


  # sample test case:
        # nums = [-2, 0, 2, 3, 4], tar = 3
        # output: 2 

        # left = 0
        # right = 4
        # mid = 2
        # nums[2] = 2 < 3 = tar

        # right = 1
        


        # nums = [0], tar = 1
        # output: -1

        # nums = [0, 10, 20], tar = 5
        # output: -1      






        


        
        