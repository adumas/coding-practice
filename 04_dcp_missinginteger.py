# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# [3] -> answer is 1
# [2] -> answer is 1
# [1] -> answer is 2
# [0] -> answer is 1
# [0,2,1] -> answer is 3
# start at 1, increment if we encounter that value


def missing_int(arr):
    missing = 1
    n = len(arr)
    for index in range(n):
        item = arr[index]
        if item > 0 and item < n:
            if item == arr[item - 1] and index > item - 1:
                # print "hey"
                arr[index] = -1 * item
            elif item - 1 != index:
                current = index
                arr[current], arr[item - 1] = arr[item - 1], arr[current]
                print index

        if item == missing:
            # print missing
            missing += 1

    print arr, missing

    for item in arr:
        if item == missing:
            missing += 1
    return missing


def test(arr, expected):
    print "===="
    print "testing " + str(arr)
    result = missing_int(arr)
    if result == expected:
        print "PASS"
    else:
        print arr
        print "FAIL" + " (" + str(result) + " != " + str(expected) + ")"


test([3, 4, -1, 1], 2)
test([1, 2, 0], 3)
test([0, 0, 1, -1, -8, 3, 16], 2)
test([0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], 5)
test([3, 4, 1, 0, 11, 2, 9, 8, 6, 7], 5)
test([1, 1, 1, 1, 1, 1, 1, 2, -10, 0, 16, 25, 11, 4, 4, 4, 4, 4], 3)
test([3, 2, 4, 5, 6, 7, 1], 8)
test([4, 3, 2, 1], 5)
