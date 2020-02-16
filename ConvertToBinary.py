def binary(num):
    if (num//2) ==0:
        return 1
    else:
        return str(binary(num//2)) + str(num%2)
    
print(binary(7))