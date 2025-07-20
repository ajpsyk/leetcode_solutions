from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = defaultdict(int)
        heap = []
        kmostfreq = []
        for num in nums:
            ht[num] += 1
        for key,v in ht.items():
            heappush(heap, (-v,key))
        for i in range(k):
            kmostfreq.append(heappop(heap)[1])
        return kmostfreq
    