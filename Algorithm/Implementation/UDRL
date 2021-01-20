# UP, DOWN, RIGHT, LEFT PROBLEM
# Given N x N size of map. Starting point is 1, 1 and given with list of directions, find the arrival point
# L = LEFT
# R = RIGHT
# U = UP
# D = DOWN
# Input example) 5
#                R R R U D D

N = int(input())
plan = list(input().split())

dir_x = [0,0,-1,1]
dir_y = [-1,1,0,0]
move_types = ['L','R','U','D']
cur_x = cur_y = 1

for d in plan:
  for i in range(len(move_types)):
    if d == move_types[i]:
      nx = dir_x[i]
      ny = dir_y[i]
      break
  
  if cur_x + nx < 1 or cur_x +nx > N or cur_y + ny < 1 or cur_y + ny > N:
    continue
  
  cur_x += nx
  cur_y += ny

print(cur_x,cur_y)
