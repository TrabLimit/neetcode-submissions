class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # thank goodness its already sorted
        
        #i = 0

        #while i < len(numbers)-1:
        #    j = i+1
        #    while j < len(numbers):
        #        if numbers[i] + numbers[j] == target:
        #            return [i+1, j+1]
        #        j += 1
        #    i += 1
        
        #return [i+1, j+1]

        # Alternative Loop:
        #for i in range(len(numbers)):
        #    for j in range(i + 1, len(numbers)):
        #        if numbers[i] + numbers[j] == target:
        #            return [i + 1, j + 1]
        #return []


        # wonder if I can do binary search?

        # From Solution:
        for i in range(len(numbers)):
            low, high = i+1, len(numbers)-1 # you can do two variables at once

            leftover = target - numbers[i]

            while low <= high:
                mid = low + (high - low) // 2
        
                # Leftover found
                if numbers[mid] == leftover:
                    return [i+1, mid+1]

                # Leftover is larger, ignore left half (since they're smaller)
                elif numbers[mid] > leftover: # elif is else if
                    high = mid - 1
                # Leftover is smaller, ignore right half (since they're larger)
                else:
                    low = mid + 1
            
        # Target not present
        return []

       


        
        