
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

def search(vertex, graph, visited):
    visited[vertex] = True

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            print(vertex, neighbour, visited)
            search(neighbour, graph, visited)

def dfs_num(graph):

    visited = {v: False for v in graph}
    a = 0
    for v in graph:
        if visited[v] == False:
            a += 1
        search(v, graph, visited)
    return a

print(dfs_num(adj_list))