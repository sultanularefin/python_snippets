# 17. Chained function call
# You can call multiple functions inside a single line.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5

print("a: ",a);
print("b: ",b);

print((subtract if a > b else add)(a, b)) # 9