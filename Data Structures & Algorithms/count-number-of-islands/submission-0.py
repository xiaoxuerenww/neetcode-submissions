class Solution:
    # DFS visit all connected land, flip them to water
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0

        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        # visit i, j and its connected land
        def DFS(i, j):
            # mark i, j as visited
            grid[i][j] = '0'

            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i+di, j+dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue            
                if grid[ni][nj] == '0':
                    continue
                DFS(ni, nj)
        
        for i in range(m):
            for j in range(n):
                # found an unvisited land
                if grid[i][j] == '1':
                    DFS(i, j)
                    num_island += 1
        return num_island

