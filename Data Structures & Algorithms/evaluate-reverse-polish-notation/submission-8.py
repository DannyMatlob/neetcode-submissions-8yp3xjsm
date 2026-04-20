class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                # Pop the second operand first
                right = stack.pop()
                # Pop the first operand second
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Use int() on float division to truncate toward zero
                    stack.append(int(left / right))
        
        return stack[0]