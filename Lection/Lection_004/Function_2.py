def f(x):
    return x*x

a = f 
print(f(5))
print(a(5))
print(type(a))



def calk1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calk1, 5, 45)
math(calk2, 5, 45)