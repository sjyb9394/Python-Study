# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.
"""
Step:
1. Add the node that has 0 indegree to the queue
2. Pop the element from the queue and delete all the out-degree edges from that element.
3. Repeat 1,2 until there are no more nodes left.
"""

# Code
from collections import deque

v,e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()

  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()

# Run Time = O(V+E)
