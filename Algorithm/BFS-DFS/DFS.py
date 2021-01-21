# Code using recursion
def DFS(graph, v, visited): # v = node, visited = bool list
  visited[v] = True
  print(v, end='')
  for i in graph[v]:
    if not visited[i]:
      DFS(graph,i,visited)


# graph = [.....] # Some graph
# visited = [False] * (number of nodes)
# DFS(graph, 1, visited) Assume 1 = start node
