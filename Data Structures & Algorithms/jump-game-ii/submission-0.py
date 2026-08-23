class Solution:
    def jump(self, nums: List[int]) -> int:

        # since we start at nums[0], does that count as 1 jump? -> no


        # test case:
        # nums = [2,1,2,3,1,1,1]
        # output = 3

        # go by level 
        # i.e. how far can I go in 1 jump / 2 jumps / etc...
        

        # level 0
        # indices I can advance from the frontier = 1, 2

        # level 1
        # indices I can advance from the frontier = 3, 4

        # level 2
        # indices I can advance from the frontier = 5, 6(end)
        

        level = 0
        curr = 0
        prev = -1
        
        while curr < len(nums)-1:
            tmp = curr
            for j in range(prev+1, curr+1): # between prev and curr
                curr = max(curr, j+nums[j])

            prev = tmp
            level += 1
        
        return level
            






        