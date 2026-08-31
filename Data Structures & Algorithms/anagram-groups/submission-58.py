class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n_dict = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            n_dict[key].append(i)
        return list(n_dict.values())
        