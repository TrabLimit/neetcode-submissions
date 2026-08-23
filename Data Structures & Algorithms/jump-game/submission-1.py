class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # is nums empty -> no
        # can nums[i] < 0 i.e. can I jump backwards -> no (but you can get stuck aka nums[i] = 0)
        # if len(nums) = 1, then is it true by default -> yes
        # so I can jump in length between 0 and nums[i] (inclusive) -> yes

        # nums = [0]
        # output = T

        # nums = [0, 1]
        # output = F

        # nums = [1, 2, 0]
        # output = T

        # nums = [1, 2, 0, 1, 0, 1]
        # output = F

        # nums = [1, 3, 0, 2, 0, 1]
        # output = T

        # nums = [5, 3, 0, 2, 0, 1]
        # output = T

        # bruteforce:
        # start at nums[0], and try every possible jump lengths to get to next point (DFS)
        # worse case, every element would have access to every element 
        # i.e. [6, 6, 6, 6, 6, 6]
        # TC = O(n^n)
        # SC = O(1)

        # optimal:
        # keep advancing to the frontier (keep track of the frontier)
        # GREEDY -> take the MAX jumplength at your current i
        # once we reach the end, then return true
        # if we reach a frontier and cannot advance any further (but still not quite at the end) return false

        # nums = [1, 3, 0, 2, 0, 1]
        # frontier = 0
        # curr = 0
        # nums[curr] = nums[0] = 1
        # frontier = max(frontier, curr+nums[curr]) = 1
        # curr += 1 -> curr = 1 

        # nums[curr] = nums[1] = 3
        # frontier = max(frontier, curr+nums[curr]) = max(1,1+3) = 4
        # curr += 1 -> curr = 2

        # nums[curr] = nums[2] = 0
        # frontier = max(frontier, curr+nums[curr]) = max(4, 2+0) = 4
        # curr += 1 -> curr = 3

        # nums[curr] = nums[3] = 2
        # frontier = max(frontier, curr+nums[curr]) = max(4, 3+2) = 5
        # curr += 1 -> curr = 4

        # nums[curr] = nums[3] = 2
        # frontier = max(frontier, curr+nums[curr]) = max(4, 3+2) = 5
        # curr += 1 -> curr = 5

        # since frontier == len(nums) -1 -> reached goal
        # return true



        # nums = [1, 2, 0, 1, 0, 1]
        # frontier = 0
        # curr = 0
        # nums[curr] = nums[0] = 1
        # frontier = max(frontier, curr+nums[curr]) = max(0, 0+1) = 1
        # curr += 1 -> curr = 1 

        # nums[curr] = nums[1] = 2
        # frontier = max(frontier, curr+nums[curr]) = max(1, 1+2) = 3
        # curr += 1 -> curr = 2

        # nums[curr] = nums[2] = 0
        # frontier = max(frontier, curr+nums[curr]) = max(3, 2+0) = 3
        # curr += 1 -> curr = 3

        # nums[curr] = nums[3] = 1
        # frontier = max(frontier, curr+nums[curr]) = max(3, 3+1) = 4
        # curr += 1 -> curr = 4

        # nums[curr] = nums[4] = 0
        # frontier = max(frontier, curr+nums[curr]) = max(4, 4+0) = 4
        # curr += 1 -> curr = 5

        # since curr > frontier 
        # (frontier cannot move any forward despite trying every step with curr)
        # return false


        frontier = 0
        curr = 0

        while curr <= frontier:

            if frontier >= len(nums) - 1:
                return True
            
            frontier = max(frontier, curr+nums[curr])
            curr += 1

        return False
















