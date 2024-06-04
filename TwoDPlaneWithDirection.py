from collections import deque

# Function to check if a given cell is valid and not blocked
def is_valid(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'

# Function to perform BFS traversal
def bfs(grid, start, dest):
    rows = len(grid)
    cols = len(grid[0])
    
    # Arrays to store visited status, parent information, and directions
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]
    direction = [[None] * cols for _ in range(rows)]
    
    # Define the directions: up, down, left, right
    directions = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
    
    # Start BFS from the start point
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        current = queue.popleft()
        if current == dest:
            break
        
        for d in directions:
            new_row = current[0] + d[0]
            new_col = current[1] + d[1]
            if is_valid(grid, new_row, new_col) and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                parent[new_row][new_col] = current
                direction[new_row][new_col] = d[2]  # Store direction
                queue.append((new_row, new_col))
    
    # Reconstruct the path from destination to start
    path = []
    current = dest
    while current:
        path.append((current, direction[current[0]][current[1]]))  # Store direction along with position
        current = parent[current[0]][current[1]]
    
    # Reverse the path to get it from start to destination
    path.reverse()
    return path

# Example grid representing the 2D plane
grid = [
    ['.', '.', '.', '.', '#'],
    ['.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.']
]

start_point = (0, 3)
destination_point = (3, 0)

# Perform BFS traversal
path = bfs(grid, start_point, destination_point)

# Print the path
print("Path from start to destination:")
for point, direction in path:
    print("Move {} to position: {}".format(direction, point))

