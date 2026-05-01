class Solution:
    def jump(self, nums: List[int]) -> int:
        # current reacheable range [l, r]
        l, r = 0, 0
        n = len(nums)
        steps = 0

        while r < n-1:
            # expand the range
            right_most = r
            for i in range(l, r+1):
                right_most = max(right_most, i + nums[i])
            # trick: update left too, because the range has been visited
            l = r + 1
            r = right_most
            steps += 1
        return steps