""" 
Given an array of integers, find the sum of its elements.
For example, if the array a= [1,2,3],1+2+3 = 6 , so return 6.

Function Description
Complete the simpleArraySum function in the editor below. 
It must return the sum of the array elements as an integer.
simpleArraySum has the following parameter(s):
ar: an array of integers 

Sample Input
6
1 2 3 4 10 11

Sample Output
31

Explanation
We print the sum of the array's elements: 1+2+3+4+10+11= 31."""


def simpleArraySum(ar):
    res = 0
    for i in ar:
        res += i
    return res


result = simpleArraySum([1, 2, 3, 4, 10, 11])
print(result)
