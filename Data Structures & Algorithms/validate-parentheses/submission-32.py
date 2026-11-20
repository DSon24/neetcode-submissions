class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for i in s:
            if i in par:
                if len(stack) == 0:
                    return False
                elif stack[-1] != par[i]:
                    return False
                else:
                    stack.pop()
            else:
                    stack.append(i)
        return len(stack) == 0
