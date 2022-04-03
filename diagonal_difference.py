""" 
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15. 
The right to left diagonal = 3+5+9=17. 
Their absolute difference is |15-17| = 2. """


def diagonalDifference(arr):
    # left to right
    ltr, rtl = 0, 0
    for i in range(len(arr)):
        ltr += arr[i][i]
    # right to left
    for i in range(len(arr)):
        rtl += arr[i][len(arr)-1-i]
    return abs(ltr-rtl)


result = diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]])
print(result)
