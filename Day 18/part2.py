# Part # 2

from collections import deque

# Read the input file
with open("inputPart2.txt", "r") as file:
    lines = file.readlines()

# Parse the falling byte positions
falling_bytes = [tuple(map(int, line.strip().split(','))) for line in lines]

# Initialize grid dimensions
GRID_SIZE = 71  # 0 to 70 inclusive
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]  # 0 for safe, 1 for corrupted

# BFS to check if a path exists
def bfs(grid, start, end):
    queue = deque([start])  # (x, y)
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False  # No path found

# Simulate falling bytes and find the blocking byte
start = (0, 0)
end = (70, 70)

for i, (x, y) in enumerate(falling_bytes):
    grid[y][x] = 1  # Mark the byte as corrupted
    if not bfs(grid, start, end):  # Check if the path is blocked
        print(f"{x},{y}")
        break