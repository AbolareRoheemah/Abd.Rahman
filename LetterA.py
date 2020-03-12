size = int(input("How big do you want your A (specify the number of lines it shoud extend): "))
i = size
star = "*"
space = " "
for s in range(0,size):
    if size % 2 == 0:
        if s == size/2:
            print(space,i*space,size*star)
    else:
        if s == (size+1)/2:
            print(space,i*space,size*star)
    print(i*space,star,2*s*space,star)
    i -= 1