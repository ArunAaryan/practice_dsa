def student(input1, input2):
    from itertools import permutations
    input2 = list(set(input2))
    input2.sort(reverse = True)
    res = []
    print(input2)
    p = list(permutations(input2, 2))
    # print(p)
    for a, b in p:
        if a > b:
            res.append((a, b))
    print(res)
    return len(res)


# res = student(10, [1,2,7,5,7,4,1,1,2,5])
res = student(10, [1,1,3,6,2])
print(res)