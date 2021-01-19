# use time library
# start_time = time.time()
# code source
# end_time = time.time()
# run_time = end_time - start_time

#Example
from random import randint
import time

array =[]
for _ in range(10000):
  array.append(randint(1,100))

start_time = time.time()  #Time start

#Section sort O(n^2)
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index],array[i]

end_time = time.time()  #Time end
print("Selection sort: ", end_time-start_time)

array =[]
for _ in range(10000):
  array.append(randint(1,100))

start_time = time.time()  #Time start
array.sort()              #Given sort algorithm worst = O(nlogn)
end_time = time.time()    #Time end
print("Library sort: ",end_time-start_time)

#=> Selection sort:  15.110008716583252
#   Library sort:  0.0013308525085449219
