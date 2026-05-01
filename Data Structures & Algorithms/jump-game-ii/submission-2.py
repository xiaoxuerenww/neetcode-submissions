from collections import deque
class Solution:
    # BFS: visit next possible index to see whether you can reach end
    # track the steps so far 
    # queue: stores next to visit
    # Time: O(N), space(N)
    def jump(self, nums: List[int]) -> int:
        # index to visit
        queue = deque([0])
        steps = 0
        n = len(nums)
        if n == 1:
            return 0
        visited = [False] * n
        visited[0] = True
        while queue:
            steps += 1
            for i in range(len(queue)):
                ind = queue.popleft()
                start = min(ind+1, n-1)
                end = min(ind + nums[ind] + 1, n)
                for j in range(start, end):
                    if j == n-1:
                        return steps
                    if not visited[j]:
                        queue.append(j)
                        visited[j] = True
        return steps 