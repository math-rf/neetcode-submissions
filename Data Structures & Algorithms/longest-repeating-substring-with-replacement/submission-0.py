class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_streak = 0
        count = {}

        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # qtd caracter mais frequente
            while r - l + 1 - maxf > k: # k caracs != mais freq
                count[s[l]] -= 1
                l += 1
            max_streak = max(max_streak, r - l + 1) 
        return max_streak



