def minimumNumberOfFlips(binaryStr):
    z_count = 0
    o_count = 0
    for val in range(len(binaryStr)):
        zstring = val % 2
        ostring = val % 2 + 1
        if int(binaryStr[val]) != zstring:
            z_count += 1
        else:
            o_count += 1
    return min(z_count, o_count)
    
res = minimumNumberOfFlips('1101')
print(res)





