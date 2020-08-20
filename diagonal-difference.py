#given a square matrix arr,
#find the absolute difference
#between the first diagonal and second diagonal

def diagonalDifference(arr):
    difference = 0

    for row in range(len(arr)):
        difference += arr[row][row] - arr[row][len(arr)-1-row]
    
    return abs(difference)

arr = [[11, 4, 2], [0, 53, 2], [6, 13, 5]]
res = diagonalDifference(arr)
print(res)
