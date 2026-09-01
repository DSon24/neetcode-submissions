class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i,0)
        
        top_k = []
        for n,c in counts.items():
            top_k.append((c,n))
        
        top_k.sort(reverse = True)

        result = []
        for i in range(k):
            result.append(top_k[i][1])
        return result
        
