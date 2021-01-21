# Given N x M array, N = row, M = column. 
# 0 represent = wall
# 1 represent = road
# Starting from (0,0) You can move only 1 square at once, find the least amount the moves that you can get to (N,M) point.
# ex) 5 6
#     101010
#     111111
#     000001
#     111111
#     111111
#   => 10


from collections import deque

N,M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int,input())))

dir_x = [-1,1,0,0]
dir_y = [0,0,-1,1]

def BFS(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dir_x[i]
      ny = y + dir_y[i]
      if nx <0 or nx>=N or ny <0 or ny>=M:
        continue

      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))

  return graph[N-1][M-1]

print(BFS(0,0))
