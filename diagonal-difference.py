#given a square matrix arr,
#find the absolute difference
#between the first diagonal and second diagonal

def diagonalDifference(arr):
    firstDiag = 0
    secondDiag = 0
    length = len(arr)

    for row in range(len(arr)):
        firstDiag += arr[row][row]
        secondDiag += arr[row][length-1-row]
    
    return abs(firstDiag-secondDiag)

arr = [[11, 4, 2], [0, 53, 2], [6, 13, 5]]
res = diagonalDifference(arr)
print(res)
