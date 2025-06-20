a = int(input("enter your number"))
b = int(input("enter your number"))
def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mul (a,b):
    return a*b
def divide(a,b):
    if b == 0:
        print("cannot divided")
    else :
        return a/b
    
add = add(a,b)
sub = sub(5,4)
mul=mul(4,5)
div = divide(6,2)
print(add)
print(sub)
print(mul)
print(div)