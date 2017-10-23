try:
    print('in try block')
    import unknown_module

    10 / 0

    variable = 'hello'
    print(variable + 10)

except (ZeroDivisionError, ImportError, TypeError):
    if ZeroDivisionError:
        print('cannot divide with 0')
    if ImportError:
        print('module not found')
    if TypeError:
        print('cannot add str and int')

        # assertions AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, this type of exception will terminate the program.

# temp = -10
# assert (temp >= 0), "Colder than absolute zero!"

# opening the file
file = open("demo.txt",
            "r")  # read mode , w - write mode, a - append mode, wb - binary mode used to write text, video files
content = file.read(10)

print(content)
# re reading. . it starts reading from where it is stopped. .  reading from 11th character here.
print(file.read())
file.close()

# reading in lines. . used to store line by line may be. .
print('reading in lines')
file = open("demo.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end="")  # extra argument end="" used to remove the extra lines

# writing files
file = open("demo1.txt",
            "w")  # creates a new file in write mode if file is not present and remove the old content if file is present
nos = file.write('Hello World!! \n Hello Mars!!')  # returns the no. of bytes it has written
print(nos)
file.close()

file = open("demo1.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()

# with statement helps to close the opened file automatically even exception occured
print('with statement')
with open("demo2.txt", "w") as f:
    f.write('writing for with statment')

with open('demo2.txt') as f:
    print(f.read())

