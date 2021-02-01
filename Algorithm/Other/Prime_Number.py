# Simple code

def is_prime_number(x):
  for i in range(2, x):
    if x % i == 0:
      return False

  return True
# Running Time = O(N)

# Using Integer's Property (We only need to check sqrt(n)
import math
def is_prime_number(x:
  for i in range(2, int(math.sqrt())+1):
    if x%i == 0:
      return Flase
  return True
# Running Time O(N^1/2)

# The sieve of eratosthenes
# Use to find all the prime numbers less than N
import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i*j] = False
      j += 1

for i in range(2, n+1):
  if array[i]:
    print(i, end = ' ')
# Running Time = O(NloglogN)
