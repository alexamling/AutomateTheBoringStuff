import os

# add new data to the file
file = open('.\\files\\text.txt', 'a')

run = True
while run:
    i: str = input().lower()
    if i == 'exit':
        run = False
    elif i == 'clear':
        file.truncate(0)
        print('File cleared')
    else:
        file.write('\n'+ i)

file.close()

# read and print file
file = open('.\\files\\text.txt', 'r')
lines = file.readlines()

print('Current contents:\n')
for line in lines:
    print(line)

file.close()

