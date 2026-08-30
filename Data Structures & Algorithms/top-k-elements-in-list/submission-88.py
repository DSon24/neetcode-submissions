class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        acc_item = []
        for i,n in freq.items():
            acc_item.append((n,i))
        
        acc_item.sort(reverse = True)
        
        result = []
        for i in range (k):
            result.append(acc_item[i][1])
        return result 
        
