def minJumps(arr, n):
  if (n <= 1):
    return 0
  if (arr[0] == 0):
    return -1
  maxReach = arr[0] 
  step = arr[0]
  jump = 1
  for i in range(1, n):
    if (i == n-1):
      return jump
    maxReach = max(maxReach, i + arr[i])
    step -= 1;
    if (step == 0):
      jump += 1
      if(i >= maxReach):
        return -1
      step = maxReach - i;
  return -1

m = n = int(input())
arr = []
while n:
    arr.append(int(input()))
    n -= 1
res = minJumps(arr, m)
print(res)