def rotate_a_matrix_by_90_degree(a):
  row_length = len(a)
  column_length = len(a[0])

  res = [[0]*row_length for _ in range(column_length)]
  for r in range(row_length):
    for c in range(column_length):
      res[c][row_length-1-r] = a[r][c]

  return res

#ex
a = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]

b = rotate_a_matrix_by_90_degree(a)
for r in b:
  print(r)
  
#[9, 5, 1]
#[10, 6, 2]
#[11, 7, 3]
#[12, 8, 4]
