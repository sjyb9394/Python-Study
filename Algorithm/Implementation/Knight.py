# Given 8 x 8 chess board. Count all possible moves for knights.
# Row = 1 ~ 8
# Column = a ~ h
# Input example) a1 // a is first column 1 is first row
#             => 2  // can move to c2 and b3

# Code
n = input()

dir = [(-2,-1),(-2,1),(-1,2),(1,2), 
      (2,-1),(2,1),(-1,-2),(1,-2)]

row = int(n[1])
col = ord(n[0]) - ord('a') + 1
count = 0

for i in range(len(dir)):
  if row + dir[i][0] >= 1 and row + dir[i][0] <=8 and col + dir[i][1] >= 1 and col + dir[i][1] <=8:
      count += 1

print(count)
