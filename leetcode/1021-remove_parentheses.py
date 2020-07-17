def removeOuterParentheses(S: str) -> str:
    stack = list()
    cant_a = 0
    cant_b = 0

    for p in S:
        if cant_a != 0:
            stack.append(p)

        if p == '(': cant_a += 1
        else: cant_b += 1

        if cant_a == cant_b:
            stack.pop()
            cant_a, cant_b = 0, 0

    return ''.join(stack)

