class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        if t_sorted == s_sorted:
            return True
        return False