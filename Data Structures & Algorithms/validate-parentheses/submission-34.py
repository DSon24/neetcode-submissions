class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        arr = []

        for i in s:
            if i in par:
                if len(arr) == 0:
                    return False
                elif arr[-1] != par[i]:
                    return False
                else:
                    arr.pop()
            else:
                arr.append(i)
        return len(arr) == 0