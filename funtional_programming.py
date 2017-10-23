def apply_twice(func, arg):
    print(2)
    return func(func(func(func(arg))))

def add_five(x):
    print(1)
    return x + 5

print(apply_twice(add_five, 10))

#lambdas
print((lambda x: x**2+2) (2))

#with multiple arguments
print((lambda x,y: x**2+y**2+2)(3,4))