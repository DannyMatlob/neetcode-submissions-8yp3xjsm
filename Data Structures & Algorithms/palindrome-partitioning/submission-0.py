class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(cur: List[str], i):
            print(cur)
            if i == len(s):
                res.append(list(cur))
                return
            
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if self.isPalindrome(substr):
                    cur.append(substr)
                    backtrack(cur, j + 1)
                    cur.pop()
        backtrack([], 0)
        return res

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l<r:
            if s[l] is not s[r]:
                return False
            l+=1
            r-=1
        return True