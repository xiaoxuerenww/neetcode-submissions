class Solution:
    """
    DP: where dp[i] is the min jumps to reach i
    update dp[i: nums[i] + i]
    time: N*M, space: N
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp  = [float('inf')] * n
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(min(n-1, i+1), min(num + i + 1, n)):
                dp[j] = min(dp[i] + 1, dp[j])
                # early termination
                if j == n-1:
                    return dp[-1]
        
        return dp[-1]
