class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                print(f"{s[l]} nao e alpha")
                l += 1
            print(f"{s[l]} e alpha")
            while r > l and not self.isAlphaNum(s[r]):
                print(f"{s[r]} nao e alpha")
                r -= 1
            print(f"{s[r]} e alpha")
            if not (s[l].lower() == s[r].lower()):
                return False
            l, r = l + 1, r - 1
        return True
    def isAlphaNum(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))

