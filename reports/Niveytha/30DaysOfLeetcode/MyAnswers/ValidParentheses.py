def isValid(s):
    # !Solution 1
    # openP = ['(', '{', '[']
    # closeP = [')', '}', ']']
    # stack = []

    # for x in s:
    #     if x in openP:
    #         stack.append(x)
    #     else:   # x in closeP
    #         if closeP.index(x) == openP.index(stack[-1]):
    #             stack.pop()
    #         else:
    #             return False

    # !Solution 2
    d = {'(':')', '{':'}','[':']'}    
    stack = []

    for x in s:
        if x in d:  # 1
            stack.append(x)
        elif len(stack) == 0 or d[stack.pop()] != x:
            return False
    return len(stack) == 0

s = "(]"
print(isValid(s))