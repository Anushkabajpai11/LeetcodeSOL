def max_sum_of_subarray(arr, n, k):
    max_sum = 0
    for i in range(0, n-k+1):
        temp = 0
        for j in range(i, i+k):
            temp += arr[j]

        if (temp > max_sum):
            max_sum = temp

    return max_sum


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
max_sum = 0

# brute force
max_sum = max_sum_of_subarray(arr, n, k)
print(max_sum)
