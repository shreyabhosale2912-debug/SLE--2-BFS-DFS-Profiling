import time
from collections import deque

# Maze Grid: 0 = Path, 1 = Wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)


# Find valid neighboring cells
def get_neighbors(cell):
    r, c = cell

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 5 and 0 <= nc < 5 and maze[nr][nc] == 0:
            yield (nr, nc)


# Breadth-First Search
def solve_bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        curr = path[-1]
        nodes_expanded += 1

        if curr == goal:
            return path, nodes_expanded

        for nxt in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])

    return None, nodes_expanded


# Depth-First Search
def solve_dfs(start, goal):
    stack = [[start]]
    visited = {start}
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        curr = path[-1]
        nodes_expanded += 1

        if curr == goal:
            return path, nodes_expanded

        for nxt in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)
                stack.append(path + [nxt])

    return None, nodes_expanded


# Profiling
if __name__ == "__main__":

    ITERATIONS = 50000

    # BFS profiling
    t0 = time.perf_counter()

    for _ in range(ITERATIONS):
        bfs_path, bfs_nodes = solve_bfs(start, goal)

    bfs_total_time = (time.perf_counter() - t0) * 1000
    bfs_avg_time = bfs_total_time / ITERATIONS

    # DFS profiling
    t0 = time.perf_counter()

    for _ in range(ITERATIONS):
        dfs_path, dfs_nodes = solve_dfs(start, goal)

    dfs_total_time = (time.perf_counter() - t0) * 1000
    dfs_avg_time = dfs_total_time / ITERATIONS


    # Comparison
    print("\n" + "=" * 70)
    print("             SLE-2 BFS vs DFS PROFILING")
    print("=" * 70)

    print(f"{'Metric':<25} | {'BFS':<15} | {'DFS':<15}")
    print("-" * 70)

    print(
        f"{'Average Time (ms)':<25} | "
        f"{bfs_avg_time:<15.6f} | "
        f"{dfs_avg_time:<15.6f}"
    )

    print(
        f"{'Nodes Expanded':<25} | "
        f"{bfs_nodes:<15} | "
        f"{dfs_nodes:<15}"
    )

    print(
        f"{'Path Length':<25} | "
        f"{len(bfs_path):<15} | "
        f"{len(dfs_path):<15}"
    )

    print("=" * 70)

    print("\nBFS Path:", bfs_path)
    print("DFS Path:", dfs_path)