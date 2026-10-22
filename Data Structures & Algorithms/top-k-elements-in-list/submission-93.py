class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        top_k = []
        for n,f in freq.items():
            top_k.append([f,n])

        top_k.sort(reverse = True)


        res = []
        for i in range (k):
            res.append(top_k[i][1])
        return res
         