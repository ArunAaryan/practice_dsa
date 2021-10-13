def rowWithMaxOnes(matrix):
    mc = [0, None]
    for row in range(len(matrix)):
        count = 0
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                count += 1
        if count >  mc[0]:
            mc[0], mc[1] = count, row
    return mc[1]
0, 0, 0, 1, 1, 1, 1, 1, 1
 
res = rowWithMaxOnes([[0, 0, 0, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 1, 1, 1, 1, 1]])
print(res)
