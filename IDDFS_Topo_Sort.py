class IterativeDeepeningTopologicalSort:
    def __init__(self):
        self.max_depth = 0
        self.topological_order = []
        self.visited = set()
        self.goal_found = False

    def iterative_deepening(self, graph):
        self.number_of_nodes = len(graph)
        while len(self.topological_order) < self.number_of_nodes:
            self.depth_limited_search(graph)
            self.max_depth += 1
        print("Topological Order:", self.topological_order[::-1])

    def depth_limited_search(self, graph):
        for node in graph:
            if node not in self.visited:
                self.dls_visit(graph, node, 0)

    def dls_visit(self, graph, node, depth):
        if node in self.visited or depth > self.max_depth:
            return
        print(f"Visiting Node: {node} at Depth: {depth}")
        self.visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in self.visited:
                self.dls_visit(graph, neighbor, depth + 1)
        self.topological_order.append(node)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    try:
        iterative_deepening_ts = IterativeDeepeningTopologicalSort()
        iterative_deepening_ts.iterative_deepening(graph)
    except ValueError:
        print("Wrong Input format")
