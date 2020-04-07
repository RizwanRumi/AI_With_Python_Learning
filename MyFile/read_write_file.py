'''
f = open('some_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)

f = open('some_file.txt', 'w')
f.write("Hello there!")
f.close()

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)

# no need to close the file by using with

with open('some_file.txt', 'r') as f:
    file_data = f.read()

print(file_data)
'''

camelot_lines = []
with open("some_file.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)