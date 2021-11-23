def romanToInteger(roman):
    number_value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    last_val  = 0
    res = 0
    n = len(roman) - 1
    while n >= 0:
        n_val = number_value[roman[n]]
        if n_val >= last_val:
            res += n_val 
        else:
            res -= n_val
        last_val = n_val
        n -= 1
    return res

res = romanToInteger('MCMIV')
print(res)
