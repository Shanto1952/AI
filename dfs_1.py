import random

def generate_grid(n, obstacles):
    grid = [[0] * n for _ in range(n)]
    for _ in range(obstacles):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        grid[x][y] = 1
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, x, y):
    n = len(grid)
    return 0 <= x < n and 0 <= y < n and grid[x][y] != 1

def dfs(grid, start, goal, visited, path):
    x, y = start
    if start == goal:
        return True
    
    visited[x][y] = True
    path.append(start)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_move(grid, nx, ny) and not visited[nx][ny]:
            if dfs(grid, (nx, ny), goal, visited, path):
                return True
    
    path.pop()
    return False

def main():
    n = int(input("Enter grid size (N): "))
    obstacles = int(input("Enter number of obstacles: "))

    grid = generate_grid(n, obstacles)
    print("Generated grid:")
    print_grid(grid)

    start = tuple(map(int, input("Enter starting position (row column): ").split()))
    goal = tuple(map(int, input("Enter goal position (row column): ").split()))

    visited = [[False] * n for _ in range(n)]
    path = []

    if dfs(grid, start, goal, visited, path):
        print("Path found:")
        for node in path:
            print(node)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
