class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        l = 0
        r = len(nums) - 1

        while l <= r:
            # caso ja ordenado
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # obtendo meio do vetor
            m = (l + r) // 2
            print(f"meio: {nums[m]}")
            res = min(res, nums[m])
            print(f"res:{res}")
            # se metade esq for a maior
            if nums[l] <= nums[m]:
                print("l < m")
                l = m + 1
            # se metade dir for a maior
            else:
                print("l >= m")
                r = m - 1
        return res
