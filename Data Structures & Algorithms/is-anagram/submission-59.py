class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s,t_t = {},{}
        for i in s:
            s_s[i] = 1 + s_s.get(i,0)
        for i in t:
            t_t[i] = 1 + t_t.get(i,0)
        if s_s == t_t:
            return True
        return False