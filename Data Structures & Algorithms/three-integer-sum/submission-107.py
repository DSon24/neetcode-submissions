class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                break
            elif i > 0 and nums[i - 1] == n:
                continue 

            j,k = i + 1, len(nums)-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ < 0:
                    j += 1
                elif summ > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
        return res



