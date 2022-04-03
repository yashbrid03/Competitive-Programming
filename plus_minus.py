""" 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
 arr = [1,1,0,-1,-1]
 
Example

There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000 , 2/5 = 0.400000 and 1/5 = 0.200000. 
Results are printed as:

0.400000
0.400000
0.200000 

"""


def plusMinus(arr):
    op = [0, 0, 0]
    for i in arr:
        if i > 0:
            op[0] += 1
        elif i < 0:
            op[1] += 1
        else:
            op[2] += 1
    print("{:.6f}".format(op[0]/len(arr)))
    print("{:.6f}".format(op[1]/len(arr)))
    print("{:.6f}".format(op[2]/len(arr)))


plusMinus([1, 1, 0, -1, -1])
