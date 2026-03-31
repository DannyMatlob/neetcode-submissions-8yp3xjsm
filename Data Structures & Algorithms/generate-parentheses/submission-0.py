class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open: int, close: int, paranthesis: str):
            if close == n:
                res.append(paranthesis)
                return
            
            if  open < n and open >= close:
                paranthesis = paranthesis + "("
                backtrack(open + 1, close, paranthesis)
                paranthesis = paranthesis[:-1]
            
            if close < open:
                paranthesis = paranthesis + ")"
                backtrack(open, close + 1, paranthesis)

        backtrack(1, 0, "(")
        return res
                
            