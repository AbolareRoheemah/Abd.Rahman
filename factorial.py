x = int(input("Enter a number to get the factorial: "))
def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num-1)

factorial = fact(x)
print(factorial)