class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i,n in enumerate(nums):
            if target - n in arr:
                return [arr[target - n],i]
            else:
                arr[n] = i
        