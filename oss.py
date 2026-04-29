#사칙연산
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("a:"))
b=int(input("b:"))
op=input("op:")
if op == '+': print(add(a,b))
if op =='-': print(sub(a,b))