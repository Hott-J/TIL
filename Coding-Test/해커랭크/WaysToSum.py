# ways to sum

total = 842
k = 91
# 1431191619
arr = [[0 for _ in range(total+1)]for _ in range(k+1)]

for i in range(1,total+1):
  arr[1][i] = 1
for i in range(1,k+1):
  arr[i][0] = 1
for row in range(2,k+1):
  for col in range(1,total+1):
    if col >= row:
      arr[row][col] = (arr[row][col-row] +arr[row-1][col])%(10**9+7)
    else:
        arr[row][col]=((arr[row-1][col]) % (10**9+7))
print(arr[k][total])