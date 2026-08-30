class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in strs:
                key = tuple(sorted(i))
                group[key].append(i)
        return list(group.values())
        