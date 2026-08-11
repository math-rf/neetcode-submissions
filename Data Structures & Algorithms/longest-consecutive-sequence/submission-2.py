class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        setNums = set(nums)
        for n in setNums:
            actual_seq = 0
            if (n-1) not in setNums:
                while(n + actual_seq) in setNums:
                    actual_seq += 1
                max_seq = max(max_seq, actual_seq)

        return max_seq
