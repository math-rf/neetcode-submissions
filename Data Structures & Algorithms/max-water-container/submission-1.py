class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_water:
                max_water = area
            else:
                if heights[l] <= heights[r]:
                    l += 1
                else:
                    r -= 1
        return max_water