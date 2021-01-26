# The array is virtually split into a sorted and an unsorted part. 
# Values from the unsorted part are picked and placed at the correct position in the sorted part.

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
print(array)

# Run Time = O(N^2), But much efficient when data is almost sorted already.
