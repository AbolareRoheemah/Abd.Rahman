def conv_to_mandarin(us_num):
    while True:
        us_num =int(input("enter the number you want to convert. Enter three zeros (200) to end: "))
        mandarin = ["ling","yi","er","san","si","wu","liu",
            "qu","ba","jiu","shi"]
        if us_num == 200:
            break
        elif us_num <= 10:
            print(mandarin[us_num])
        elif us_num > 10 and us_num < 20:
            evaluate = (us_num - 10)
            print(mandarin[-1] +" "+ mandarin[evaluate]) 
        elif us_num >= 20:
            translator = list(str(us_num))
            if translator[-1] == '0':
                print(mandarin[int(translator[0])] +" "+ mandarin[-1])
            else:
                print(mandarin[int(translator[0])] +" "+ mandarin[-1] +" "+ mandarin[int(translator[-1])])
            

conv_to_mandarin("us_num")            