
# file = open('demo.txt', mode='r')
# file = open('demo.txt', mode='a')
# file.write('Hello from Python\n')
# file_content = file.read()
# file_content = file.readlines()
# print(file_content)
# Return the first line
# file_content = file.readline()

# for line in file_content:
    # print(line)

with open('demo.txt', mode='r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
print('Done!')


file.close()

