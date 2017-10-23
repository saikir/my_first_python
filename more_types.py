# dictionaries

# in dictionary it wont follow order like list and tuples

dic = {0: "Sai", 'key': 'Kiran', 5: 2, 'combi': 'SaiKiran', }

print(dic)

if 0 in dic:
    print('yes')
else:
    print('no')

if "Sai" not in dic:
    print("Sai is not in dic as a key")

# get in lists
print(dic.get(0))
print(dic.get("key", "not found"))
print(dic.get("key1", "not found"))

print(dic.get(5, 4) + dic.get(7, 2))

# only immutable objects can be assign as keys to dictionaries eg. String or int; as lists and dictionaries are called as mutable objects
# immutable and mutable eg.
string1 = "myString"
string2 = string1
string1 = "my2ndString"

print("string1 :" + string1)
print("string2 :" + string2)

list1 = [1, 2, 3]
list2 = list1
list1.append('a')
print(list1)
print(list2)
# both list1 and list2 got affected.


# tuples are immutable lists; means they cant grow their size once assigned
tuple1 = (1, 2, 3, 4, 'string1')
tuple2 = 1, 2, 3, 4, 'string1'

if tuple1 == tuple2:
    print('same')

# since tuples are immutable, we can assign them as a key in dictionaries. we can add a mutable list and dictionary as an element in tuples.
tuple3 = (1, 2, 3, 4, 'string1', [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], {'name': 'SaiKiran', 'age': '24'})
print('tuple3 : ' + str(tuple3))

# list slices it can be done on lists and tuples
print(tuple3[5][2:8:2])

print(list1[::2])
print(tuple3[1:6:2])

# negative slices
print(tuple1[::-1])  # reversing the tuple
print(tuple3[1::-1])
print(tuple1[
      1:-1])  # it starts to count from the index 1 to the last index, hiding the last element like a standard slice.

# list comprehensions
cubes = [i ** 3 for i in range(10)]
print('cubes')
print(cubes)

evens = [i for i in range(50) if i % 2 == 0]
print('evens')
print(evens)

# printing multiples of 3
multiples_of_3 = [i for i in range(30) if i % 3 == 0]
print('multiples of 3')
print(multiples_of_3)

# string formatting
nums = [4, 5, 6]
strnums = 'Numbers {0}, {1} and {2}'.format(nums[0], nums[1], nums[2])
print(strnums)

# string formatting can be done with names arguments
print('sum is {x}+{y}'.format(x=2, y=3))

# Useful functions
# split and join
stringsj = 'chicken, mutton, fish,'
string_split = stringsj.split(',')
print(string_split)  # returns a list
print(len(string_split))
string_join = 'biryani'.join(string_split)
print(
    string_join)  # returns a string  IF WE WONT ADD THE COMMA AFTER FISH WHILE ASSINGING stringsj IT WONT ADD biryani TO FISH

if stringsj.endswith('fish,'):
    print(True)
if string_join.startswith('chicken'):
    print("Chicken started")

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"


# demonstration of all and any used in lists
list1 = [50, 35, 25, 18]
if all(i > 15 for i in list1):
    print('all numbers in list1 is greater than 15')

if any(i % 2 == 0 for i in list1):
    print('any one number in list1 is even')

for v in enumerate(list1):
    print(v)

for v in enumerate(list1, -1):  # using enumerator we can specify what index you want to start with
    print(v)