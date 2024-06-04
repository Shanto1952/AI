class IterativeDeepeningPathFinder:
    def __init__(self):
        self.max_depth = 0
        self.path = []
        self.found = False

    def iterative_deepening(self, graph, source, destination):
        self.max_depth = 0
        while not self.found:
            self.path = []
            self.found = self.depth_limited_search(graph, source, destination, 0)
            self.max_depth += 1
        print(f"Path Found: {' -> '.join(self.path)}")

    def depth_limited_search(self, graph, node, destination, depth):
        if depth > self.max_depth:
            return False
        self.path.append(node)
        if node == destination:
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in self.path:  # Prevent cycles
                if self.depth_limited_search(graph, neighbor, destination, depth + 1):
                    return True
        self.path.pop()
        return False

if __name__ == "__main__":
    graph = {}
    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break
        neighbors = input(f"Enter the neighbors of {node} separated by spaces: ").upper().split()
        graph[node] = neighbors

    source = input("Enter the source node: ").upper()
    destination = input("Enter the destination node: ").upper()

    if source not in graph or destination not in graph:
        print("Source or destination node not in graph.")
    else:
        path_finder = IterativeDeepeningPathFinder()
        path_finder.iterative_deepening(graph, source, destination)
