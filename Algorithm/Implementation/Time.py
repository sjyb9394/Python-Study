# Given input N, from 00(h) : 00(m) : 00(s) to N(h) : 59 (m) : 59(s), count if any digit contain number 3.

N = int(input())
count = 0

for i in range(N+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        print(str(i)+" "+str(j)+" "+str(k))
        count+=1
print(count)
