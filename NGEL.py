def nearest_greater_to_left(arr):

  result = []

  for i in range(0, len(arr)):

    for j in range(i-1,-1,-1):

      if arr[i] < arr[j]:

        result.append(arr[j])

        break

    else:

      result.append(-1)

  return result

arr = [1, 3, 2, 5, 4]

print(nearest_greater_to_left(arr))