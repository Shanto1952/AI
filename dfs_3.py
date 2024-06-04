def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def topological_sort(graph):
    visited = {node: False for node in graph}
    stack = []
    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, stack)
    return stack[::-1]

def main():
    # Example graph representing the 2D plane
    graph = {
        (0, 0): [(1, 0), (0, 1)],
        (1, 0): [(1, 1)],
        (0, 1): [(1, 1)],
        (1, 1): [(2, 1)],
        (2, 1): []
    }

    topological_order = topological_sort(graph)
    print("Topological order of node traversal:")
    for node in topological_order:
        print(node)

if __name__ == "__main__":
    main()
