class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # is coin sorted -> No (assume)
        # coins will have only positives -> yes 
        # what is the expected length of coins -> <= 10 (can iterate without too much runtime issues)
        # will coins be empty? -> no
        # can an amount be 0 -> yes (non-negative)
        # will coins and amount be in float range -> yes
        # is it possible for all coins to sum to the target -> No. in which case return -1
        # is there a limit to how much for each coin can I use? -> No.  unlimited number of each coin.
        # is there guarantee that the amount is greater than or equal to smallest of coins -> No

        # test case:
        # coins: [1], amount: 0
        # output: 0

        # coins: [2], amount: 1
        # output: -1

        # coins: [1, 2], amount: 4
        # output: 2

        # coins: [1, 6], amount: 4
        # output: 4

        # coins: [2], amount: 3
        # output: -1


        
        # Brute force:
        # try with every coin 
        # DFS
        # duplicate calculation
        # max level = amount / smallest coin
        # each level has #coin brannches
        # worst case, the tree is #coin ^ (max level+1) -1 
        # -> exponential (BAD)


        # optimal:
        # 1. set up an array of length = amount + 1 (let amount = 12 for this example)
        # 2. set array[12] = 0, rest unknown (infinity or whatever)
        # 3. Go backwards so array[11] is accessible to array[12] in 1 step, array[10] in 2 steps, and etc.
        # at array[11] we have access to 1, 5, 10 and we know the # of coins so far to reach array[11], so that would be 1 + array[12] (or 1+ array[index after])
        # 4. if your next index (backwards) has -1, then there wouldn't be any way to reach that state, so skip and move the next index
        # 5. If we get array[0] != -1, then we have found a way (in fact with the fewest step) to reach the target, so we can just return array[0]
        # 6. if we kept iterating and reached array[0] by iteration and it's still -1 then there was no way to have reached that target so return -1 (or just return array[0] since we set it as -1, at least for this problem's case)


        #[3, 2, 1, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0]

        # runtime analysis: 
        # 1.  we make array size of amount, and populate them with -1 (except the final index) -> O(amount) (this is size complexity)
        # 2. For every array[i], we fill at most # coins entries 
        # 3. we keep filling the array until array[0] is filled (or everything else is filled) 
        # for each iteration we will fill out # coins times
        # for amount + 1 times you will iterate all the coins
        # (amount+1)*|coins| = O(amount*coins) (since amount+1 is just O(amount))

        data = [-1] * (amount+1)
        data[amount] = 0

        for i in range(amount, 0, -1): # iterating backwards
            for coin in coins:
                if i-coin >= 0 and data[i] != -1:
                    if data[i-coin] == -1:
                        data[i-coin] = 1 + data[i]
                    else:
                        data[i-coin] = min(data[i-coin], 1 + data[i])

            
                
        # print(data)
        return data[0]






             



        



        





        