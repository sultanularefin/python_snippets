import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25
print(action['**'](2, 4)) # 25