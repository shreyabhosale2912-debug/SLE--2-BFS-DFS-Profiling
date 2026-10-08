import cProfile
import pstats

from benchmark import solve_bfs, solve_dfs, start, goal


def profile_bfs():
    for _ in range(1000):
        solve_bfs(start, goal)


def profile_dfs():
    for _ in range(1000):
        solve_dfs(start, goal)


print("=== BFS Profiling ===")
cProfile.run("profile_bfs()", "bfs_profile.prof")

stats_bfs = pstats.Stats("bfs_profile.prof")
stats_bfs.sort_stats("cumtime")
stats_bfs.print_stats(10)


print("\n=== DFS Profiling ===")
cProfile.run("profile_dfs()", "dfs_profile.prof")

stats_dfs = pstats.Stats("dfs_profile.prof")
stats_dfs.sort_stats("cumtime")
stats_dfs.print_stats(10)