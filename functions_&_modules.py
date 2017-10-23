def says():
    return 'hello'


def say(animal, nature):
    """
    returns the voice of animals
    """
    if (animal == 'dog'):
        return nature + ' Bhow! Bhow!'
    elif (animal == 'cat'):
        return nature + ' Meow!'
    elif (animal == 'lion'):
        return nature + ' Whraaarr!!'


animals = ['dog', 'cat', 'lion', ]
nature = 'domestic'

for ani in animals:
    if ani == 'lion':
        nature = 'wild'
    print(ani + ' says ' + say(ani, nature))

# unline java we can rename the function names in python
talks = says
print('human said ' + talks())


# functions can be passed as arguments
def add(x, y):
    return x + y


def double_add(func, a, b):
    return func(func(a, b), func(a, b))


print(double_add(add, 10, 5))

# modules
import random as rnd
# import control_structures
from control_structures import test_function, dummy  # importing required functions from modules

for i in range(5):
    print(rnd.randint(1, 6))
print(test_function() + ' ' + dummy())

