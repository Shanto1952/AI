def dfs(graph, source, destination, visited, path):
    if source == destination:
        return True
    
    visited.add(source)
    path.append(source)

    for neighbor in graph[source]:
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, visited, path):
                return True
    
    path.pop()
    return False

def find_path(graph, source, destination):
    visited = set()
    path = []

    if dfs(graph, source, destination, visited, path):
        return path
    else:
        return None

def main():
    # Example graph representing connections between nodes
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    source = 'A'
    destination = 'F'

    path = find_path(graph, source, destination)

    if path:
        print("Path from", source, "to", destination, ":", path)
    else:
        print("No path found from", source, "to", destination)

if __name__ == "__main__":
    main()

# DFS