def add(a, b):
    if type(a) and type(b) is not int:
        raise TypeError("the value must be int only..")
    return a + b


def sub(a, b):
    try:
        if type(a) and type(b) is not int:
            raise TypeError("the value must be int only..")
    except TypeError:
        print("type error..")

    return a - b

def mul(a, b):
    if type(a) is not int:
        raise TypeError("the value must be int only..")
    elif type(b) is not int:
        raise TypeError("the value must be int only..")
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("The divisor must not be zero")
    if type(a) and type(b) is not int:
        raise TypeError("the value must be int only..")
    return a / b

'''a=int(input('enter value a:'))
b=int(input('enter value b:'))
c=int(input('please choose the value,1 for add, 2 for sub, 3 for mul,4 for div\n'))
if c==1:
    addition=add(a,b)
    print("The addition of a Given Number {0} ".format(addition))
elif c==2:
    subtraction=sub(a,b)
    print("The subtraction of a Given Number {0} ".format(subtraction))
elif c==3:
    multiplication=mul(a,b)
    print("The multiplication of a Given Number {0} ".format(multiplication))
elif c==4:
    division=div(a,b)
    print("The division of a Given Number {0} ".format(division))
'''
