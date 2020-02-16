def speed_checker(speed):
    while True:
        speed = int(input("What is the speed of the car: "))
        if speed <= 70:
            print("Ok!")
        elif speed > 70:
            point = int((speed - 70)/5)
            if point < 12:
                print("You have " + str(point) + " demerit points")
            else:
                print("License suspended ")
                break

speed_checker("speed")     

