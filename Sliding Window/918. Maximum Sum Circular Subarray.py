class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = minSum = maxSum = currMin = currMax = nums[0]
        for num in nums[1:]:
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
            total += num
        return  max(maxSum, total - minSum) if maxSum > 0 else maxSum