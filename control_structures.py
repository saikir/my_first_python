"""x = input('enter x : ')
y = input('enter y : ')
if x>y:
    print('x is greater')
elif x<y:
    print('y is greater')
else:
    print('both are equal')

#Boolean logic
if not 1==1 and 2+2<5:
    print(True)
else:
    print(False)"""

# while loop
i = 1
while i <= 5:
    print('before increment ' + str(i))
    i += i
    # i=i+1
    print('after increment ' + str(i))
print('finished')

# continue : Basically continue stops the current iteration and continues with the next one.

# Lists
my_list = ['I', 'Love', 'India', ]
print(my_list[1])

my_big_list = [my_list, 'and', 'America', ]
print(my_big_list)
print(my_big_list[0][1])

my_very_big_list = [my_big_list, 'very', 'much']
print(my_very_big_list[0][0][1])

# strings can be print as lists
dummy_string = 'girlfriend'
print(dummy_string[5])

# dummy_string[5] = dummy_string[0] 'str' object does not support item assignment
# print(dummy_string)


# in operator ---- used to check whether the given word/phrase/piece of word in a list/string
print('America' in my_big_list)  # True
print('America' in my_very_big_list)  # false returns true only when it is directly present in that list.
print('girl' in dummy_string)

my_very_big_list[0][2] = 'India again :)'
print(my_very_big_list)

print('line 54 ' + str(not 'America' in my_big_list))

if 'India' in my_list:
    print('yes it is!!')

# -------------------------------------List Functions-------------
my_list.append('appended value')
print(my_list)

print(len(my_list))  # len is a function we need to pass the objects into it
print(len(dummy_string))

my_list.insert(1, 'inserted value')
print(my_list)

print(dummy_string.index('i'))

nums = [20, 15, 18, 21, 9]
print(max(nums))
print(min(nums))
print(len(nums))
print(my_list.count('India'))
my_list.remove('inserted value')
print(my_list)

my_list.reverse()
print(my_list)

# ----------Range----------
print(range(
    10))  # The call to list is necessary because range by itself creates a range object, and this must be converted to a list if you want to use it as one.

range_ = list(range(3, 30, 3))
print(range_)

# for loop instead of forloop we can use counter variable with while.
forreplace = ['eggs', 'spam', 'boiled eggs']
max_index = len(forreplace) - 1
counter = 0
while counter <= max_index:
    print(forreplace[counter])
    counter = counter + 1

for forloop in forreplace:
    print(forloop + '!')

# to repeat an iteration for some lines we use range
for i in range(5):
    print('hello')


def test_function():
    return "testing"


def dummy():
    return "dummer"