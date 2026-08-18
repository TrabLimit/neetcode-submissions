class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # so can nums have negative or 0 -> No. Between 2 and 30.
        # can target be 0 or negative -> No. Between 2 and 30.
        # is nums empty -> no
        # is nums sorted? -> no 
        
        # nums = [1]
        # target = 2
        # output = [[1,1]]

        # nums = [2]
        # target = 7
        # output = [] # impossible

        # nums = [2, 3, 4]
        # target = 8
        # output = [[2, 2, 2, 2], [2, 4, 2], [2, 3, 3], [4, 4]]


        # DFS: optimal solution just becomes brute force

        # terminal case: 
        # 1. target - sum so far = 0 (success)
        # 2. target - sum so far < 0 (you've gone too far, so pop back up)



        # nums = [2,5,6,9], target = 9

        # result = []
        # curr = []
        # sum = 0

        # target - sum = 9 

        # i = 0
        # curr = [2], sum = 2
        
        # target - sum = 7
        # curr = [2, 2], sum = 4

        # target - sum = 5
        # curr = [2, 2, 2], sum  = 6

        # target - sum = 3
        # curr = [2, 2, 2, 2], sum = 8

        # target - sum = 1
        # curr = [2, 2, 2, 2, 2], sum = 10

        # target - sum = -1 < 0
        # curr pop -> curr = [2, 2, 2, 2], sum -= 2 => sum = 8

        # target - sum = 1
        # i = 1
        # curr append 5 -> curr = [2, 2, 2, 2, 5],, sum = 13

        # target - sum = -4
        # i = 2
        # curr pop -> curr = [2, 2, 2, 2], sum -= 5 => sum = 8

        # runtime: 
        # max depth = ceiling of target / smallest num
        # branching factor = |nums| = n
        # O (n^ (target / smallest num))



        result = []
        curr = []
        total = [0]

        def dfs(i):

            if i >= len(nums):
                return

            if target - total[0] == 0:
                result.append(curr.copy())
                return
            
            if target - total[0] < 0:
                return
            
            total[0] += nums[i]
            curr.append(nums[i])
            dfs(i)

            total[0] -= nums[i]
            curr.pop()
            dfs(i+1)

        dfs(0)

        return result
                









