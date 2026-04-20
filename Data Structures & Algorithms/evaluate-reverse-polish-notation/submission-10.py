class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token)) # Convert to int immediately to save time
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Use float division then cast to int to truncate toward zero
                    stack.append(int(num1 / num2))
        
        return stack[0]