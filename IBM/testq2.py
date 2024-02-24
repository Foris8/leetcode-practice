import math


def minCost(arr):
    maxDiff = 0
    index = -1
    n = len(arr)
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) > maxDiff:
            maxDiff = abs(arr[i] - arr[i + 1])
            index = i

    median = (arr[index] + arr[index + 1]) // 2

    initialCost = 0
    for i in range(n - 1):
        initialCost += math.pow(arr[i] - arr[i + 1], 2)

    # Adjust the initial cost for the pair with the maximum difference
    initialCost = (initialCost - math.pow(arr[index] - arr[index + 1], 2) +
                   math.pow(arr[index] - median, 2) +
                   math.pow(median - arr[index + 1], 2))

    return initialCost

# Example usage
arr = [1, 3, 5, 2, 10]
print(minCost(arr))  # Replace this with actual numbers to test
