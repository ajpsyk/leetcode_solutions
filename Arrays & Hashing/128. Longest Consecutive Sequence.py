from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put nums in set to remove duplicates
        nums_set = set(nums)
        # longest_seq
        longest_seq = 0
        # iterate over set
        for num in nums_set:
            # if num is start of sequence (there is no num - 1)
            if num - 1 not in nums_set:
                # set curr_seq = 1
                curr_seq = 1
                # set curr = num
                curr = num
                # while there is a num + 1
                while curr + 1 in nums_set:
                    # increase sequence and curr by 1
                    curr_seq += 1
                    curr = curr + 1
                # update longest sequence if needed
                longest_seq = max(longest_seq, curr_seq)
        # return longest_seq
        return longest_seq