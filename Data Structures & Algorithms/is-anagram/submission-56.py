class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_t,arr_s = {},{}
        for i in s:
            arr_s[i] = 1 + arr_s.get(i,0)
        for i in t:
            arr_t[i] = 1 + arr_t.get(i,0)
        if arr_s == arr_t:
            return True
        return False