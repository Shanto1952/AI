from collections import deque

# Define a function to check if a cell is valid (not an obstacle)
def is_valid(grid, row, col):
    # ... implementation to check if the cell is within bounds and not an obstacle
    pass
# Function to find the topological order (BFS exploration)
def find_traversal_order(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]  # Keep track of visited cells
    queue = deque([(0, 0)])  # Start from the origin
    traversal_order = []

    while queue:
        row, col = queue.popleft()
        if visited[row][col]:
            continue
        visited[row][col] = True
        traversal_order.append((row, col))

        # Explore valid neighbors in all directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and is_valid(grid, new_row, new_col) and not visited[new_row][new_col]:
                queue.append((new_row, new_col))

    return traversal_order

# Example usage (replace with your actual grid data)
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0],
]

traversal_order = find_traversal_order(grid)
print("Traversal Order:", traversal_order)
