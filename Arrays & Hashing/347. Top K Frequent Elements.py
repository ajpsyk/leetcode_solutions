from collections import Counter
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        heap = []
        kmostfreq = []
        for key,v in freq_table.items():
            heappush(heap, (-v,key))
        for _ in range(k):
            kmostfreq.append(heappop(heap)[1])
        return kmostfreq
    