class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = n * [0]
        suf = n * [0]
        result = n * [0]

        pref[0] = suf[n-1] = 1

        for i  in range (1,n):
            pref[i] = pref[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i] = suf[i +1 ]* nums[i+1]
        for i in range (n):
            result[i] = pref[i] * suf[i]
        return result
         