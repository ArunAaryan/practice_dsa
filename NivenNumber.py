def niven_number(n):
    nc = n
    sum = 0
    while n:
        r = n % 10
        sum += r
        n //= 10
    return nc // sum


res = niven_number(57)
print(res)
