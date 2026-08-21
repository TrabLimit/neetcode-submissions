class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        minimum = nums[0]
        minIndex = 0
        
        # find minimum first (cutline)

        while left <= right:
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] < nums[minIndex]:
                minIndex = mid

            if nums[0] > nums[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
              
        
        print (minimum)
        print (minIndex)

        # 2 binary searches for each segment
        # left segment
        left1 = 0
        right1 = minIndex - 1
        while left1 <= right1:
            mid1 = (left1 + right1) // 2
            
            if target == nums[mid1]:
                return mid1
            if target < nums[mid1]:
                right1 = mid1 - 1
            else: 
                left1 = mid1 + 1

        
        #2. right segment
        left2 = minIndex
        right2 = len(nums) - 1
        while left2 <= right2:
            mid2 = (left2 + right2) // 2
            
            if target == nums[mid2]:
                return mid2
            if target < nums[mid2]:
                right2 = mid2 - 1
            else: 
                left2 = mid2 + 1



        return -1


        