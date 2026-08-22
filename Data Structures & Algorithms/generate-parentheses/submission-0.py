class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # can n be 0 -> no

        # 2 choices: open or close
        # at start you can only open 
        # when you closed all open (open == close) you can only open
        # when open == n, you can only close
        # once open == close == n, append curr to result

        # n = 3
        # result = []
        # curr = ""
        # o = 0
        # c = 0
        
        # call dfs(0,0)
        # since o == c -> append "(" to curr and o++

        # call dfs(1,0)
        # curr = "("
        # o = 1
        # c = 0
        # since o = 1 != c so 2 choices -> open first
        # curr = "(("
        
        # call dfs(2,0)
        # o = 2
        # c = 0
        # since o = 2 != c so 2 choices -> open first
        # curr = "((("

        # call dfs(3,0)
        # o = 3
        # c = 0
        # since o = 3 = n, but c = 0 != n so we can only continue with close
        # curr = "((()"

        # call dfs(3,1)
        # o = 3
        # c = 1
        # since o = 3 = n, but c = 1 != n so we can only continue with close
        # curr = "((())"

        # call dfs(3,2)
        # o = 3
        # c = 2
        # since o = 3 = n, but c = 2 != n so we can only continue with close
        # curr = "((()))"

        # call dfs(3,3)
        # o = 3
        # c = 3
        # since o == c == 3, append curr to result

        # return to dfs(3,2)
        # remove ")" from curr (since c has decremented)

        # return to dfs (3,1)
        # remove ")" from curr (since c has decremented)

        # return to dfs (3,0)
        # remove ")" from curr (since c has decremented)

        # return to dfs (2,0)
        # remove "(" from curr (since o has decremented)
        # try the next choice -> close
        # curr = "(()"

        # call dfs(2,1)
        # o = 2
        # c = 1
        # since o = 2 != c so 2 choices -> open first
        # curr = "(()("

        # call dfs(3,1)
        # o = 3
        # c = 1
        # since o = 3 = n, but c = 1 != n so we can only continue with close
        # curr = "(()()"

        # call dfs(3,2)
        # o = 3
        # c = 2
        # since o = 3 = n, but c = 2 != n so we can only continue with close
        # curr = "(()())"

        # call dfs(3,3)
        # o = 3
        # c = 3
        # since o == c == 3, append curr to result

        # return to dfs(3,2)
        # remove ")" from curr (since c has decremented)

        # return to dfs (3,1)
        # remove "("" from curr (since o has decremented)

        # call dfs(2,1)
        # o = 2
        # c = 1
        # since o = 2 != c next choice -> close
        # curr = "(())"

        # call dfs(2,2)
        # o = 2
        # c = 2
        # since o = 2 = c so you can only open
        # curr = "(())("

        # call dfs(3,2)
        # o = 3
        # c = 2
        # since o = 3 = n, but c = 2 != n so we can only continue with close
        # curr = "(())()"

        # call dfs(3,3)
        # o = 3
        # c = 3
        # since o == c == 3, append curr to result

        # return to dfs(3,2)
        # remove ")" from curr (since c has decremented)

        # return to dfs (2,2)
        # remove "("" from curr (since o has decremented)

        # return to dfs (2,1)
        # remove ")" from curr (since c has decremented)

        # return to dfs (2,0)
        # remove ")" from curr (since c has decremented)

        # return to dfs (1,0)
        # remove "(" from curr (since o has decremented)


        # call dfs(1,0)
        # curr = "("
        # o = 1
        # c = 0
        # next choice close 
        # curr = "()"

        # call dfs(1,1)


        # at the end return result

        # TC:
        # 2 branches
        # tree depth = 2n (n open n close)
        # but you only get branching n times (when there's open) (because when you use up all the open, then all you can do is close)

        # so O(2^n + n)?

        # SC:


        result = []
        curr = ""

        def dfs(curr, o, c):

            if o > n or c > n or o < c: # invalid
                return

            if o == n and c == n:
                result.append(curr) # no need to copy string since this is NOT array so not passed by reference but passed by value?
                return
            
            if o == n: # close only
                curr += ")"
                dfs(curr, o, c+1)
                curr = curr[:-1]
                return
                
            if c == o: # open only
                curr += "("
                dfs(curr, o+1, c)
                curr = curr[:-1]
                return

            curr += "("
            dfs(curr, o+1, c)
            curr = curr[:-1]

            curr += ")"
            dfs(curr, o, c+1)
            curr = curr[:-1]
    
        dfs(curr, 0, 0)

        return result

            
            

        
            

        