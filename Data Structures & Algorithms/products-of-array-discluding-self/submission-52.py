class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suf = [0]*n
        res = [0]*n
        pref[0] = suf[n-1] = 1
        for a in range (1,n):
            pref[a] = pref[a - 1] * nums[a-1]
        for b in range (n-2,-1,-1):
            suf[b] = suf[b +1 ] * nums[b+1]
        for i in range(n):
            res[i] = pref[i] * suf[i]
        return res
