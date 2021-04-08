

def solution(s):
    c = s[0]
    if not c.isdigit() and c.isupper():    # please fix condition
        return "upper"
    elif not c.isdigit() and c.islower():  # please fix condition
        return "lower"
    elif c.isdigit():  # please fix condition
        return "digit"
    else:
        return "other"


#print(solution("abcd"))
print(solution("1bcd"))