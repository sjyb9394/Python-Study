# Given N, K, find least amount of number of how many operations are needed to make n => 1.
# Rule:
# 1) If N % K == 0, Divide N by K
# 2) Else, subtract N by 1

#Code
n, k = map(int, input().split())
count = 0
while n > 1:
  if n % k == 0: n //= k
  else: n -= 1
  count +=1
print(count)

#Code 2
n, k = map(int, input().split())
result = 0

while True:
  target = (n//k) * k
  result += (n - target)
  n = target
  
  if n < k:
    break
  
  result += 1
  n //= k

result += (n-1)
print(result)




  
