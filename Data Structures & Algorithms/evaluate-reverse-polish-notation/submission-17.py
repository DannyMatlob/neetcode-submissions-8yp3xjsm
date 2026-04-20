class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda x,y: x+y, 
            "-": lambda x,y: x-y, 
            "*": lambda x,y: x*y, 
            "/": lambda x,y: int(x/y)
        }
        for token in tokens:
            if token in operators:
                right, left = stack.pop(), stack.pop()
                op = operators[token]
                stack.append(op(left,right))
            else:
                stack.append(int(token))
        
        return stack[0]