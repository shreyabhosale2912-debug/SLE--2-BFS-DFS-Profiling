from collections import deque

# Maze Grid: 0 = Path, 1 = Wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start, goal = (0, 0), (4, 4)

def get_neighbors(cell):
    r, c = cell
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and maze[nr][nc] == 0:
            yield (nr, nc)

# --- Breadth-First Search (BFS) ---
def solve_bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()  # FIFO
        curr = path[-1]
        
        if curr == goal:
            return path
            
        for nxt in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])
    return None

# --- Depth-First Search (DFS) ---
def solve_dfs(start, goal):
    stack = [[start]]
    visited = {start}
    
    while stack:
        path = stack.pop()  # LIFO
        curr = path[-1]
        
        if curr == goal:
            return path
            
        for nxt in get_neighbors(curr):
            if nxt not in visited:
                visited.add(nxt)
                stack.append(path + [nxt])
    return None

print("BFS Shortest Path Length:", len(solve_bfs(start, goal)))
print("DFS Path Length:", len(solve_dfs(start, goal)))