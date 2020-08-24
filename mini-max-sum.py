def miniMaxSum(arr):
    #given 5 positive integers, find the min/max sums of 4

    sumOfArr = sum(arr)
    minSum = sumOfArr
    maxSum = 0

    for i in range(5):
        currentSum = sumOfArr - arr[i]

        if currentSum < minSum:
            minSum = currentSum
        if currentSum > maxSum:
            maxSum = currentSum

    return minSum, maxSum

print(miniMaxSum([10, 50, 3, 0, 5]))
