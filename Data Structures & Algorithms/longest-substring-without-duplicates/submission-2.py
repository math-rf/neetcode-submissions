class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streak = set()
        high_streak = 0
        left = 0
        for right in range(len(s)):
            while s[right] in streak:
                streak.remove(s[left])
                left += 1
            streak.add(s[right])
            high_streak = max(high_streak, len(streak))

        return high_streak

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9"))