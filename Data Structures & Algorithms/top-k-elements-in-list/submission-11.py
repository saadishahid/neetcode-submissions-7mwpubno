class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = {}
        res = []

        for n in nums:
            if n not in num_count:
                num_count[n] = (1,n)
            else:
                num_count[n] = (num_count[n][0] + 1, n)
        
        freq_list = list(num_count.values())

        heapq.heapify_max(freq_list)

        for i in range(k):
             res.append(heapq.heappop_max(freq_list)[1])
        return res


