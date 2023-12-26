def solve(inputString):
    stackList = list()
    for i in inputString:
        if i == '(':
            stackList.append(')')
        elif i == '[':
            stackList.append(']')
        elif i == '{':
            stackList.append('}')
        elif stackList and stackList.pop() != i:
            return False
    return not stackList

print(solve('(((((())))))[]{}'))
print(solve('(((((())))[]{}'))



