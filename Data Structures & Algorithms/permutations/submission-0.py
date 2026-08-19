class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        # can num be negative or 0 -> yes
        # is num sorted -> no
        # can nums be empty -> no

        # nums = [1]
        # output = [[1]]

        # nums [1, 2]
        # output = [[1,2], [2,1]]

        # nums = [1, 2, 3, 4]
        # output = 
        # [[1,2,3,4],[1,2,4,3],[1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2],
        # [2,1,3,4],[2,1,4,3],[2,3,1,4], [2,3,4,1], [2,4,1,3], [2,4,3,1],
        # [3,1,2,4],[3,1,4,2],[3,2,1,4], [3,2,4,1], [3,4,1,2], [3,4,2,1],
        # [4,1,2,3],[4,1,3,2],[4,2,1,3], [4,2,3,1], [4,3,1,2], [4,3,2,1]]


        # so take the nums (array), cast it to a set (so no order or duplicates)
        # traverse through the set, take the element and add to run-in array and remove from set
        # keep doing until the set is empty
        # once set is empty then you added all so add the current runin array to result
        # then pop back up 


        # adding and removing an element from a set takes O(1) time
        # there are n! possible permutations 
        # TC: O(n!)
        # SC: n! permutations have n elements each -> O(n*n!)

        result, curr = [], []
        numSet = set(nums)
        def dfs():
            if len(numSet) == 0: # if empty
                result.append(curr.copy())
                return
            
            for num in list(numSet): # whatever iterate over doesn't get impacted by what you add or remove
                curr.append(num)
                numSet.remove(num)
                dfs()
                numSet.add(num)
                curr.pop() 
        dfs()
        return result
            









