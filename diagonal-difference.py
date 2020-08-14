def diagonalDifference(arr):
    # Write your code here
    firstDiag = 0
    secondDiag = 0

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if col==row:
                firstDiag += arr[row][col]
            if col+row == len(arr)-1:
                secondDiag += arr[row][col]
    
    return abs(firstDiag-secondDiag)

arr = [[11, 4, 2], [0, 53, 2], [6, 13, 5]]
res = diagonalDifference(arr)
print(res)
