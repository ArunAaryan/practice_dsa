def ReversedCharacters(cls, input1):
    new_res = ''
    for word in input1.split(' '):
        reversed_word = word[::-1]
        reversed_word = reversed_word.capitalize()
        new_res += reversed_word + ' '
    return new_res[:-1]

res = ReversedCharacters('cls','Hello World')
print(res)
res = ReversedCharacters('something','are you sure you don\'t want to come for the party?')
print(res)


