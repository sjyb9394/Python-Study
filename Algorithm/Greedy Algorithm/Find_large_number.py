#Given N = size of array, M = number of addition, K = maximum amount of repeated number, find the largest sum.
# ex) given array = [2,4,5,4,6] M = 8, K = 3 => 6+6+6+5+6+6+6+5 => 46


# 1 Using for loop
n,m,k = map(int,input().split())
l = list(map(int,input().split()))
sum = 0

l.sort()
for i in range(m):
  if (i+1) % k == 0:
    sum += l[-2]
  else:
    sum += l[-1]

print(sum)


# 2 Using equation int(m (k+1) * k) + m % k + 1
n,m,k = map(int,input().split())
l = list(map(int,input().split()))
sum = 0

l.sort()
first = l[n-1]
second = l[n-2]

count = int(m/(k+1))*k
count += m % (k+1)

sum += (count) * first
sum += (m-count) * second

print(sum)

