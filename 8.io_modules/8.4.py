
n = 10
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]

visited = [False] * n

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if adj_list[v][i] == 1 and not visited[i]:
            dfs(i)

ans = 0
for i in range(n):
    if not visited[i]:
        ans += 1
        dfs(i)

print(ans)