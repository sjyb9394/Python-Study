#Finding largest number among the 2d array.
# Rules:
# 1. Given N x M array. N = row, M = column
# 2. Select the row first.
# 3. Pick the smallest number from that row.
# 4. Repeast this for all rows, and find the largest number among the selected numbers.

# Code
n,m = map(int,input().split())
result = 0

for i in range(n):
  b = list(map(int,input().split()))
  temp = min(b)
  result = max(temp, result)

print(result)



