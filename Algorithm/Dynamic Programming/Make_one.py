# Given integer input N: compute following 4 operations and find the least amount the operations to make 1.
# 1. If x % 5 == 0 divide by 5
# 2. If x % 3 == 0 divide by 3
# 3. If x % 2 == 0 divide by 2
# 4. Subtract by 1

n = int(input())
d = [0] * 30001

for i in range(2, n+1):
  d[i] = d[i-1]+1
  if i % 2 == 0:
    d[i] = min(d[i],d[i//2]+1)
  if i% 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i% 5 == 0:
    d[i] = min(d[i], d[i//5]+1)

print(d[[n]])

