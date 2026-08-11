class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        print(result)
        pos = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == pos:
                    continue
                result[j] *= nums[i]
            pos += 1
        return result