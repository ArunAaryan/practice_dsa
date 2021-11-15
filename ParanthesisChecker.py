def checkParanthesis(x):
    open_brackets = ['(', '{', '[']
    closed_brackets = [')', '}', ']']
    st = []
    for bracket in x:
        if bracket in open_brackets:
            st.append(bracket) 
        else:
            if not st:
                return False            
            last_bracket = st.pop()
            if last_bracket != open_brackets[closed_brackets.index(bracket)]:
                return False
    if st:
        return False
    else:
        return True

res = checkParanthesis('(({}))')
print(res)


