def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum


result = aVeryBigSum(
    [1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
print(result)
