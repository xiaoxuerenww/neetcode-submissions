class Solution:
    """
    sliding window, narrow down the left and right by moving the shorter bar
    """
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            area = (r-l) * min(heights[r], heights[l])
            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area