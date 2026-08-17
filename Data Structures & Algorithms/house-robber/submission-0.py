class Solution:
    def rob(self, nums: List[int]) -> int:
        # can nums be empty? -> no
        # are elements of nums in float range -> yes
        # is nums sorted -> no
        # does nums have duplicates -> yes
        # can nums have negative -> no (but it can have 0)
        
        # test case:
        # nums: [1]
        # output: 1

        # nums: [1, 2]
        # output: 2

        # nums: [1, 4, 2]
        # output: 4

        # nums: [3, 1, 2, 4]
        # output: 7

        # brute force:
        # you do DFS but with branches being potential next house
        # in example nums = [2,9,8,3,6]
        # if you pick 2, then branches would be [8,3,6]
        # if you pick 8, then it's [6]
        # for 3 you have nothing []

        # the depth of the tree is at most n/2 (skipping every next house)
        # branching factor is at most n-2 (exclusing itself and the adjacent) or O(n)
        # so the runtime is O(n)^(n/2) => O(n^n)

        # Optimal solution:
        # scenario 1 : 1 element in the array -> choose that element
        # scenario 2 : 2 elements -> pick the max between the two
        # scenario 3 : 3 elements -> pick either 1,3 or just 2


        # each entry we'll keep track of the max sum you can get up to and including that entry

        # [3, 1, 2, 4]
        # new: [3, max(3,1) = 3, max(3, 3+2) = 5, max(5, 4+3)]
        # choose the max between previous and (current + 2 entries ago)
        # time complexity = O(n) since we just iterate once -> single pass
        # space complexity = O(1) all we need is previous and previous previous entry

        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = curr
            curr = max(prev + nums[i], curr)
            prev = temp
        
        return curr        

        # [3, 1, 2, 4]
        # prev = 3
        # curr = 3

        # i=2
        # temp = 3
        # curr = max (3+2, 1) = 5
        # prev = 3

        # i=3
        # temp = 5
        # curr = max (3+4, 5) = 7
        # prev = 5





        



        