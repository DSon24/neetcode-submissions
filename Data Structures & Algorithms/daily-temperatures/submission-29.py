class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                old_i, old_t = stack.pop()
                res[old_i] = i - old_i
            stack.append((i,n)) 
        return res