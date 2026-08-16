class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        for i in range(len(s)):

            # push the open bracket to stack
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                stack.append(s[i])

            # check if the closed bracket is present, 
            # and if it matches then pop, if not it's impossible
            elif s[i] == ')':
                if stack:
                    # print(stack[-1])
                    if stack[-1] == '(':
                        stack.pop()
                    else: 
                        return False
                else:
                    return False

            elif s[i] == ']':
                if stack:
                    # print(stack[-1])
                    if stack[-1] == '[':
                        stack.pop()
                    else: 
                        return False
                else:
                    return False

            elif s[i] == '}':
                if stack:
                    # print(stack[-1])
                    if stack[-1] == '{':
                        stack.pop()
                    else: 
                        return False
                else:
                    return False
            else:
                continue
        
        return not stack 
        # it should be empty if all brackets negate each other
        

                

                 


        
        