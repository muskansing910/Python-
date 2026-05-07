temp = int(input("Enter Temperature:"))

if temp>0:
    if temp>=21:
        if temp>30:
            print("Temperature Status : HOT")
        else:
            print("Temperature Status : WARM")
    else:
        print("Temperature Status : COLD")
else:
    print("Temperature Status : FREEZING")