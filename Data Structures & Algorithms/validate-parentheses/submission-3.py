class Solution:
    def isValid(self, s: str) -> bool:
        stack_open = []
        map_bracket = {")": "(",
                        "]": "[",
                        "}": "{"}
        for c in s:
            if len(s) % 2 != 0:
                return False
            if c in map_bracket:
                if stack_open and stack_open[-1] == map_bracket[c]:
                    stack_open.pop()
                else:
                    return False
            else:
                stack_open.append(c)
        if stack_open:
            return False
        return True