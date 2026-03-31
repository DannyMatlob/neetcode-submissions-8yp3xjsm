class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxFreq = 0
        res = 0
        l = r = 0

        for r in range(len(s)):
            count[s[r]] = count[s[r]] + 1
            maxFreq = max(maxFreq, count[s[r]])
            print(count, maxFreq)
            while (r - l + 1) - maxFreq > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            res = max(r - l + 1, res)
        
        return res