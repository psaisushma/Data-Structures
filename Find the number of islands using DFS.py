def num_islands(grid):
    if not grid:
        return 0
    def dfs(grid, i, j):
        if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == '0'):
            return
        grid[i][j] = '0'
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)
    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                island_count += 1
    return island_count

grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "0"],
    ["0", "0", "0", "1"],
    ["0", "1", "0", "1"]
]
print(num_islands(grid))