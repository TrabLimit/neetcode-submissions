class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # is the tokens always syntatically (in terms of math) correct? -> Yes
        # are the any operators beyond +, -, * and /? -> no
        # are there any parentheses in the expression -> no

        # could the operands be letters or variables? -> no
        # is the operand always positive -> no could be negative

        # should we assume that expression is always valid -> yes

        # could there be division by 0 -> not sure

        # token [1]
        # output: 1

        # token [1, 2, /]
        # output 1 / 2 = 0


        # solution

        # use stack 
        # detect operators then use operation

        stack = []

        arg1 = 0
        arg2 = 0
        result = 0


        for i in range(len(tokens)):
            if tokens[i] == "+":
                arg2 = stack.pop()
                arg1 = stack.pop() 
                result = arg1 + arg2
                stack.append(result)

            elif tokens[i] == "-":
                arg2 = stack.pop()
                arg1 = stack.pop() 
                result = arg1 - arg2
                stack.append(result)
            
            elif tokens[i] == "*":
                arg2 = stack.pop()
                arg1 = stack.pop() 
                result = arg1 * arg2
                stack.append(result)

            elif tokens[i] == "/":
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = abs(arg1) // abs(arg2)
                if (arg1 < 0 and arg2 > 0) or (arg1 > 0 and arg2 < 0):
                    result *= -1
                
                stack.append(result)

            else:
                result = int(tokens[i])
                stack.append(result)
        
        return stack[-1]

            



        
        