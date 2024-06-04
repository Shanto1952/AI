
class IterativeDeepeningDFS:
    def __init__(self):
        self.max_depth = 0
        self.visited = set()

    def iterative_deepening(self, graph):
        start_node = input("Enter the start node: ").upper()
        self.max_depth = 0
        while True:
            print(f"\nDepth-Limited Search at Depth: {self.max_depth}")
            self.visited = set()
            if self.depth_limited_search(graph, start_node, 0):
                break
            self.max_depth += 1

    def depth_limited_search(self, graph, node, depth):
        if depth > self.max_depth:
            return False
        print(f"Visiting Node: {node} at Depth: {depth}")
        self.visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in self.visited:
                if self.depth_limited_search(graph, neighbor, depth + 1):
                    return True
        return False

if __name__ == "__main__":
    graph = {}
    while True:
        node = input("Enter a node (or 'done' to finish): ").upper()
        if node == 'DONE':
            break
        neighbors = input(f"Enter the neighbors of {node} separated by spaces: ").upper().split()
        graph[node] = neighbors

    iterative_deepening_dfs = IterativeDeepeningDFS()
    iterative_deepening_dfs.iterative_deepening(graph)
