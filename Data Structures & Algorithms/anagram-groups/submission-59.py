class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            s[key].append(i)
        return list(s.values())
        