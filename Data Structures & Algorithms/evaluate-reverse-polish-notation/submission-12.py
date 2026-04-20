class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            print(stack, token)
            if token not in operators:
                stack.append(int(token))
                continue
            
            num2, num1 = stack.pop(), stack.pop()
            
            if token == "+":
                stack.append(num1 + num2)
            elif token == "-":
                stack.append(num1 - num2)
            elif token == "*":
                stack.append(num1 * num2)
            elif token == "/":
                stack.append(int(num1 / num2))
        
        return stack[0]