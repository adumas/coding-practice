def unique_bst(n):
    num_of_bst = [0] * (n + 1)
    num_of_bst[0] = num_of_bst[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            num_of_bst[i] += num_of_bst[j - 1] * num_of_bst[i - j]

    return num_of_bst[n]


print unique_bst(3)
print unique_bst(4)
