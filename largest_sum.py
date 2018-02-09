# Largest Sum

# two large integers (strings)
# return sum as string

# input: string1 and string2
# output: result_string
#
#
# Input: str1 = "3333311111111111"
# Input: str2 = "44422222221111"

# Output: "3377733333332222"

# Time Complexity: O(max(m,n))
# Auxiliary Space Complexity: O(max(m,n))

# str1 = '1111'
# str2 = '2222'
# out  = '3333'

# str1 = '999'
# str2 = '101'
# out = '1100'


# # example 1
# str1 = '111111'
# str2 =      '2'

# # 1st pass
#   str1[5] + str2[5-diff]
#   str1[5] + str2[0]

# # 2nd pass
#   str1[4] + str2[4-5]
#   should be


# # pseudocode


# swap if str2 longer than str1

# diff = |len(str1) - len(str2)| = 5
# loop index in max(string lengths) : -1 : 0

#     str1[4] if index-diff is negative

#     else

#     current_sum = str1[index] + str2[index-diff]

#     if carry is True
#       sum + 1

#     if > 9
#       carry = True

#     # sum of digits at index
#     output = sum + output

#   return output

def largest_sum(str1, str2):
    output = ''

    # swap if str2 larger
    if len(str2) > len(str1):
        str2, str1 = str1, str2

    # loop through and sum
    diff = len(str1) - len(str2)
    # print str2[len(str1) - diff]
    # print len(str1), len(str2), diff
    carry = 0
    for index in range(len(str1) - 1, -1, -1):
        # print index, index - diff
        # print str2[index - diff]

        if index - diff < 0:
            current_sum = carry + int(str1[index])
        else:
            current_sum = carry + int(str1[index]) + int(str2[index - diff])

        if current_sum > 9:
            carry = 1
        else:
            carry = 0
        current_sum = str(current_sum % 10)
        output = current_sum + output

    return output


print largest_sum('3333311111111111', '44422222221111')
