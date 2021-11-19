import math
def getCarResaleValue(cost, year, rate):
    if type(year) == type(cost) == int and rate >= 5 and rate <= 100:
        while year - 1:
            cost -= (cost * rate)/ 100
            year -= 1
        return math.ceil(cost)
    else:
        return 'Invalid input'


res = getCarResaleValue(485000, 5, 5)
print(res)