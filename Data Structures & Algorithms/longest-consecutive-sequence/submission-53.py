class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                initial = 1
                while i + initial in nums:
                    initial += 1
                longest = max(longest, initial)
        return longest
