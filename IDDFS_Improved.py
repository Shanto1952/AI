class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.number_of_nodes = 0
        self.depth = 0
        self.max_depth = 0
        self.goal_found = False

    def iterative_deepening(self, graph, destination):
        self.number_of_nodes = len(graph)
        while not self.goal_found:
            print(f"\nDepth-Limited Search at Depth: {self.max_depth}")
            self.depth_limited_search(graph, 'A', destination)
            self.max_depth += 1
        print(f"\nGoal Found at Depth {self.depth}")

    def depth_limited_search(self, graph, source, goal):
        self.stack.append((source, 0))
        while self.stack:
            element, depth = self.stack.pop()
            if depth <= self.max_depth:
                print(f"Visiting Node: {element} at Depth: {depth}")
                if element == goal:
                    self.goal_found = True
                    self.depth = depth
                    return
                for neighbor in graph[element]:
                    self.stack.append((neighbor, depth + 1))

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H'],
        'E': ['I'],
        'F': ['J', 'K'],
        'G': ['L'],
        'H': ['M', 'N'],
        'I': [],
        'J': [],
        'K': [],
        'L': [],
        'M': [],
        'N': []
    }
    try:
        destination = input("Enter the destination for the graph: ").upper()
        if destination not in graph:
            print("Destination node not found in the graph.")
        else:
            iterative_deepening = IterativeDeepening()
            iterative_deepening.iterative_deepening(graph, destination)
    except ValueError:
        print("Wrong Input format")
