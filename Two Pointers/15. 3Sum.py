from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize threeSums
        threeSums = []
        # sort the array
        nums.sort()
        # set a pointer to start, end, and middle
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            middle = i + 1
            end = len(nums) - 1
            # while end != middle
            while middle < end:
                # if the sum of the three is too big
                total = nums[i] + nums[middle] + nums[end]
                if total > 0:
                    # decrement end
                    end -= 1
                # if the sum of the three is too small
                elif total < 0:
                    # increment start
                    middle += 1
                # if equal
                else:
                    # add the three to the list
                    threeSums.append([nums[i], nums[middle], nums[end]])
                    middle += 1
                    while nums[middle] == nums[middle - 1] and middle < end:
                        middle += 1
        return threeSums