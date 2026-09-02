class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                old_i,old_n = stack.pop()
                res[old_i] = i - old_i
            stack.append([i,n])
        return res
