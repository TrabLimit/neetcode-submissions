class Solution:
    def findMin(self, nums: List[int]) -> int:
        # do I know how many times it was rotated -> no
        # is nums empty -> no
        # is nums unique -> yes
        # is nums in float range -> yes
        # is nums only positive integers -> no you can have 0 or negative

        # test case:
        # nums = [1]
        # output = 1

        # nums = [1, 2, 3]
        # output = 1

        # nums = [9, 11, 2, 3, 4, 7]
        # nums = [4, 7, 9, 11, 2, 3]
        # output = 2

        # Bruteforce: O(n)
        # you iterate every element and keep track of the min

        # Optimal:
        # keep track of left, mid, and right
        # at start left = 0, right = len(nums)-1  mid = (left + right) /2,

        # while left < right
        
        # if nums[left] > nums[mid]; then mid is on right segment: every number to the right is going be bigger -> check to the left (right is mid-1)
        # if nums[left] < nums[mid]: then mid is on the left segment: there exists a smaller number to the right -> check to the right (left is mid + 1)

        
        # return mid


        left = 0
        right = len(nums) - 1
        minimum = nums[0]
        
        while left <= right:
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if nums[0] > nums[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
                
        
        return minimum



        