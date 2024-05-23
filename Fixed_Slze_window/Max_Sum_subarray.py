# find the max sum of subarray of size K

def max_sum_subarray(arr, k):
    n = len(arr)
    # base Condition
    if n < k:
        return 0

    max_sum = float('-inf')
    curr_sum = 0
    i = 0
    j = 0
    max_subarray = []
    while j < n:
        curr_sum += arr[j]

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            max_sum = max(max_sum, curr_sum)
            if curr_sum == max_sum:
                max_subarray = arr[i:j+1]
            curr_sum -= arr[i]
            j += 1
            i += 1
    return max_sum, max_subarray


arr = [2, 5, 1, 8, 2, 9, 1]
k = 3
print(max_sum_subarray(arr, k))
