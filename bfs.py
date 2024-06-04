from collections import deque

def print_direction(m, x, y):
    if m == 0:
        print("Moving Down ({}, {})".format(x, y))
    elif m == 1:
        print("Moving Up ({}, {})".format(x, y))
    elif m == 2:
        print("Moving Right ({}, {})".format(x, y))
    else:
        print("Moving Left ({}, {})".format(x, y))

def st_bfs(graph, source, directions, x_move, y_move, N, goal):
    queue = deque([source])
    visited = set([source])
    path = {}  # To track the path to each node
    path[source] = None  # Source has no parent

    while queue:
        u = queue.popleft()
        u_x, u_y = u

        if u == goal:
            # Reconstruct the path from goal to source
            optimal_path = []
            while u is not None:
                optimal_path.append(u)
                u = path[u]
            optimal_path.reverse()
            return True, optimal_path

        for j in range(directions):
            v_x = u_x + x_move[j]
            v_y = u_y + y_move[j]

            if (0 <= v_x < N) and (0 <= v_y < N) and graph[v_x][v_y] == 1 and (v_x, v_y) not in visited:
                v = (v_x, v_y)
                queue.append(v)
                visited.add(v)
                path[v] = u  # Set u as the parent of v
                print_direction(j, v_x, v_y)

    return False, []  # Goal not found

def init():
    graph = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ]
    N = len(graph)
    print(N)
    source_x = 0
    source_y = 2
    goal_x = 4
    goal_y = 0
    source = (source_x, source_y)
    goal = (goal_x, goal_y)

    found, optimal_path = st_bfs(graph, source, 4, [1, -1, 0, 0], [0, 0, 1, -1], N, goal)

    if found:
        print("Goal found")
        print("Optimal shortest path:")
        for node in optimal_path:
            print("({}, {})".format(node[0], node[1]))
    else:
        print("Goal cannot be reached from the starting block")

init()