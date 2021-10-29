def loveSeventeen(S):
    number_map = {}
    for num in S:
        val = int(num)
        if val in number_map:
            number_map[val] += 1 
        else:
            number_map[val] = 1 
    print(number_map)
    for num in number_map.keys():
        req = 17 - num
        if req in number_map and number_map[req] > 0 and number_map[num] > 0:
            remove = min(number_map[req],number_map[num])
            number_map[req] -= remove
            number_map[num] -= remove
    print(number_map)
    left = 0
    for val in number_map:
        left += number_map[val] 
    return left


print(loveSeventeen('389889'))