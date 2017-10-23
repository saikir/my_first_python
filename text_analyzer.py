def count_char(readed_data, char):
    counter = 0;
    for a in readed_data:
        if a == char:
            counter += 1;
    return counter

file = open('demo1.txt','r')
readed_data =  file.read()
char = input('enter the searching char')
print(count_char(readed_data, char))
file.close()