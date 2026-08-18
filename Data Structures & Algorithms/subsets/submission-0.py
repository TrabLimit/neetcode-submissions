class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # does num contain negative or 0? -> yes (range from -10 to 10)
        # does is num sorted? -> no
        # is num empty? -> no
        # nums contain unique integers
        

        # test case:
        # nums = [1]
        # output = [[], [1]]

        # nums = [0, 1, 2]
        # output = [[], [0], [0, 1], [0, 1, 2], [1], [1, 2], [2]]


        # brute force:
        # loop over every element and make a subset out of them
        # dangerous -> potentially double calculate
        # runtime: O(n^2)

        # optimal:
        # for every element, you have 2 choices: add or not add
        # so runtime is O(2^n)

        # nums = [0, 1, 2]

        # make curr = []
        # make result = []
        
        # i = 0 
        # add 0 to curr -> curr = [0]
        # i = 1
        # add 1 to curr -> curr [0, 1]
        # i = 2 
        # add 2 to curr -> curr [0, 1, 2]

        # i = 3 
        # base case hit 
        # add curr [0, 1, 2] to result
        # result = [[0, 1, 2]]

        result = []

        curr = []

        def dfs(i: int):
            if i == len(nums):
                result.append(curr.copy()) # since we pass by reference, so we pass the copy so any modification to curr is not affecting the original
                return
            
            # 1. add the element
            curr.append(nums[i])
            dfs(i+1)

            # 2. skip the element
            # make sure you pop the previously added nums[i]
            curr.pop()
            dfs(i+1)
        
        dfs(0)

        return result
    


 




        
