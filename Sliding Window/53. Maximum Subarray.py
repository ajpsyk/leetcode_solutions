class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum, 0)
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum
        