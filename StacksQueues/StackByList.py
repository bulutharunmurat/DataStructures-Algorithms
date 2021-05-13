def checkParantheses(expression):
    stack = []
    try:
        for char in expression:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
    except IndexError:
        return False

    return len(stack) == 0