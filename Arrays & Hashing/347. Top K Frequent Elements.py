from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashTable
        ht = defaultdict(int)
        # key is unique value, value is frequency
        # create kmostfrequentelements list
        kmostfreq = []

        # iterate over nums
        for num in nums:
            # add each num to hasTable, update frequency
            ht[num] += 1
        # check hashTable k times
        for _ in k:
            # define max val at -1
            maxVal = -1
            maxKey = 0
            # define max key at 0
            # iterate over hashTable
            for k,v in ht.items():
                # if value is bigger than max
                if k not in kmostfreq and v > maxVal:
                    # max is value
                    maxVal = v
                    # max key is key
                    maxKey = k
            # append max key to kmostfreq
            kmostfreq.append(maxKey)
        # return kmostfreq
        return kmostfreq