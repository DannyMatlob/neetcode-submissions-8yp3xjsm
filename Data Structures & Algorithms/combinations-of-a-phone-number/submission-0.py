class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(curStr: str, i: int):
            if i == len(digits):
                if curStr:
                    res.append(curStr)
                return
            
            possibleChars = keys[digits[i]]
            for j in range(len(possibleChars)):
                nextStr = (curStr if curStr else "") + possibleChars[j]
                backtrack(nextStr, i + 1)
        
        backtrack("", 0)
        return res