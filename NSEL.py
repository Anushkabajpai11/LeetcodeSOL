def nearest_smaller_to_left(arr):
    result = []
    for i in range(0, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                result.append(arr[j])
                break
        else:
            result.append(-1)

    return result

arr = [6, 4, 10, 2, 5]
print(nearest_smaller_to_left(arr))