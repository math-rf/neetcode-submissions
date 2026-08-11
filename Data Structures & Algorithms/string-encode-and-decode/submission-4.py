class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + ";" + word
        return res
    def decode(self, s: str) -> List[str]:
        list_words = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != ";":
                j += 1
            print(i, j)
            length = int(s[i:j])
            print(s[i])
            list_words.append(s[j + 1: j + 1 + length]) 
            i = j + 1 + length
        return list_words         



