class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        rank = []
        for n,f in freq.items():
            rank.append([f,n])
        
        rank.sort(reverse = True)

        top_k = []
        for i in range(k):
            top_k.append(rank[i][1])
        return top_k