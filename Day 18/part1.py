#Part # 1

from collections import deque

# Read the input file
with open("inputPart1.txt", "r") as file:
    lines = file.readlines()

# Parse the falling byte positions
falling_bytes = [tuple(map(int, line.strip().split(','))) for line in lines]

# Initialize grid dimensions
GRID_SIZE = 71  # 0 to 70 inclusive
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]  # 0 for safe, 1 for corrupted

# Simulate the first 1024 bytes falling
for i in range(min(1024, len(falling_bytes))):
    x, y = falling_bytes[i]
    grid[y][x] = 1  # Mark corrupted

# BFS to find the shortest path
def bfs(grid, start, end):
    queue = deque([(*start, 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y, steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # No path found

# Start and end points
start = (0, 0)
end = (70, 70)

# Find and print the minimum steps
min_steps = bfs(grid, start, end)
if min_steps != -1:
    print(f"The minimum number of steps to reach the exit is: {min_steps}")
else:
    print("No path to the exit exists.")
