def miniMaxSum(arr):
    #given 5 positive integers, find the min/max sums of 4

    maxSum = 0
    minSum = sum(arr)
    sumOfArr = minSum

    for i in range(5):
        currentSum = sumOfArr - arr[i]

        if currentSum < minSum:
            minSum = currentSum
        if currentSum > maxSum:
            maxSum = currentSum

    print(minSum, maxSum)

miniMaxSum([10, 50, 3, 0, 5])