class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        str = []
        while l < len(word1) and r < len(word2):
            str.append(word1[l])
            str.append(word2[r])
            l += 1
            r += 1
        str.append(word1[l:])
        str.append(word2[r:])
        return "".join(str)