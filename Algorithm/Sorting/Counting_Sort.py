#Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). 
#Then doing some arithmetic to calculate the position of each object in the output sequence.

array = [7,5,9,0,3,1,6,2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')
    
#Run Time : O(N+K) = Very fast but efficient when only you know the range of the data
