"""
def binary(num):
    if (num//2) ==0:
        return 1
    else:
        return str(binary(num//2)) + str(num%2)
    
print(binary(7))
"""
with open('learning_python.txt') as file_object:
    contents = file_object.read()    
    print(contents)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line)

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.replace("Python","java"))