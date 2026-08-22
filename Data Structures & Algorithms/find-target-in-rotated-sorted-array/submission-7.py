class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # left = 0
        # right = len(nums) - 1
        # minimum = nums[0]
        # minIndex = 0
        
        # # 1. find minimum first (cutline)

        # while left <= right:
        #     mid = (left + right) // 2
        #     minimum = min(minimum, nums[mid])

        #     if nums[mid] < nums[minIndex]:
        #         minIndex = mid

        #     if nums[0] > nums[mid]:
        #         right = mid - 1
                
        #     else:
        #         left = mid + 1
              
        
        # print (minimum)
        # print (minIndex)

        # # 2. TWO binary searches for each segment

        # # 2a. left segment BS
        # left1 = 0
        # right1 = minIndex - 1
        # while left1 <= right1:
        #     mid1 = (left1 + right1) // 2
            
        #     if target == nums[mid1]:
        #         return mid1
        #     if target < nums[mid1]:
        #         right1 = mid1 - 1
        #     else: 
        #         left1 = mid1 + 1

        
        # # 2b. right segment BS
        # left2 = minIndex
        # right2 = len(nums) - 1
        # while left2 <= right2:
        #     mid2 = (left2 + right2) // 2
            
        #     if target == nums[mid2]:
        #         return mid2
        #     if target < nums[mid2]:
        #         right2 = mid2 - 1
        #     else: 
        #         left2 = mid2 + 1



        # return -1




        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # we know left seg's start is at 0, and right seg's end is at end of nums
            # we don't know where the boundary between the 2 segments are

            if nums[mid] == target: # base case
                return mid

            if nums[0] <= nums[mid]: # this means that mid is on the left
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: # it has to be right side
                    left = mid + 1
            
            else: # mid is on the right segment
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else: # it has to be left side
                    right = mid - 1
        
        return -1 # if not found
                    
                


        