class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                initial = 1
                while initial + i in nums:
                    initial += 1
                length = max(length, initial)
        return length