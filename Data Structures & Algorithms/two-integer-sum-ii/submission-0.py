class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0

        while i < len(numbers)-1:
            j = i+1
            while j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                j += 1
            i += 1
        
        return [i+1, j+1]
        
        