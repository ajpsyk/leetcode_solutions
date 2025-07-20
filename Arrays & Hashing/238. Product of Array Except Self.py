from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create prefix array
        prefixes = []
        product = 1
        for num in nums:
            product *= num
            prefixes.append(product)
        # create postfix array
        postfixes = []
        product = 1
        for num in nums[::-1]:
            product *= num
            postfixes.append(product)
        # create output array
        output = []
        # iterate over nums
        product = 1
        for i in range(len(nums)):
            if i - 1 > -1 and len(nums) - 2 - i > -1:
                prefix = prefixes[i - 1]
                postfix = postfixes[len(nums) - 2 - i]
                product = prefix * postfix
                output.append(product)
            elif i - 1 < 0:
                output.append(postfixes[len(nums) - 2 - i])
            else:
                output.append(prefixes[i - 1])
            # prefix at i - 1 multiplied by postfix at len(nums) - 1 - i
            # append product to output
        return output
    
solution = Solution()
solution.productExceptSelf([1,2,3,4])