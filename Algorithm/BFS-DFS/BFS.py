# Code using queue
from collections import deque

def BFS(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
 
#graph = [....] somegraph
#visited = [False] * (number of nodes)
#BFS(graph,1,visited) Assume 1 = starting node
