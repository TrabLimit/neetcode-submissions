class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # does num contain negative or zero -> yes
        # can num be empty -> no. it has at least one
        # is num sorted -> no
        # is the product contiguous (cannot skip element?) -> yes
        # are we returning the subarray -> no just the product 
        # are nums and output in the floating range -> yes
        # if there is a single number what do I return -> that element (it must be a product of at least one element in nums)


        # test case:
        # nums: [-1]
        # output: -1

        # nums: [2, 0, -2, 5]
        # output: 5

        # nums: [2, 3,  0, -2, 4]
        # output: 6


        # brute force:
        # for every element, try every possible subarrays and get the maximum product
        # [2, 3,  0, -2, 4]
        # 2, 2*3, 2*3*0, 2*3*0-2, 2*3*0*-2*4
        # 3, 3*0, 3*0*-2, 3*0*-2*4, 
        # 0, 0*-2, 0*-2*4, 
        # -2, -2*4,
        # -4

        # there are n+...+2+1 potential subarrays which O(n^2)
        


        # optimal algorithm:
        # you start at the beginning of the array 
        # and chose the first element as the largest product at this step (pos)
        # and chose the first element as the smallest product at this step (neg)
        # we also preserve the max product thus far, ans (at start this would be first element)
        # CAUTION: also keep track of min product thus far: 
        # WHY? because the next element might have negative sign that may flip the product. 
        # we iterate over i through the array (curr = nums[i])
        # pos = max(nums[i], nums[i]*pos, nums[i]*neg) 
        # neg = min(nums[i], nums[i]*pos, nums[i]*neg) 
        # ans = max(ans, pos)

        # return ans at the end


        # [-5, -2, -1, -3]
        # i = 0
        # Before:
        # curr = -5
        # posProd = empty
        # negProd = empty
        # ans = -inf
        # After:
        # posProd = -5
        # negProd = -5
        # ans = max(ans, posProd) = -5

    
        # i = 1
        # Before:
        # curr = -2
        # posProd = -5
        # negProd = -5
        # ans = -5
        # After:
        # posProd = max(curr, curr*pos, curr*neg) = 10
        # negProd = min(curr, curr*pos, curr*neg) = -2
        # ans = max(ans, posProd) = 10

        # i = 2
        # Before:
        # curr = -1
        # posProd = 10
        # negProd = -2
        # ans = 10
        # After:
        # posProd = max(curr, curr*pos, curr*neg) = 2
        # negProd = min(curr, curr*pos, curr*neg) = -10
        # ans = max(ans, posProd) = 10

        # i = 3
        # Before:
        # curr = -3
        # posProd = 2
        # negProd = -10
        # ans = 10
        # After:
        # posProd = max(curr, curr*pos, curr*neg) = 30
        # negProd = min(curr, curr*pos, curr*neg) = -6
        # ans = max(ans, posProd) = 30

        # return 30

        ans = float('-inf')
        pos, neg = None, None

        for i in range(len(nums)):
            pos, neg = max(nums[i], nums[i]*pos, nums[i]*neg) if pos else nums[i], min(nums[i], nums[i]*pos, nums[i]*neg) if neg else nums[i]
            ans = max(ans, pos)
        
        return ans








        


        