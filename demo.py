print ('hi')
print(22/7) #comment
"""multiline comment
can be done by keeping three double quotes"""
print(22//7) #can be called floor division output is 3.
print(22%7) #called as modulo division gives remainder.
print("test 'ducking' string");
#Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.
print('test "rocking" string')
print("test \"testing\" string\nnew line")

#testing the three quotes without backslash n
print("""testing
the 
three quotes
without backslash n""")

print('print(print("printing()")');


#print(input());

print(int('2')*float('3'))
#print(int(input("Enter an int"))*2)

#declaring a runtime variable
x = input('Enter a number')
print('twice of the entered number is : ' + x*2) #prints string twice
print(int(x)*2)

spam = "two eggs"
print (spam)
#del spam          #del the variable
#print(spam)

#In-Place Operators
y = int(x)
y /= 2
print("inplace operator" + str(y))
spam += ' eggs'
print('string inplace operator :' + spam);

