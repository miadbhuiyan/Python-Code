height = int(input("Enter Your Height "))
if height >= 3:
    print("Can Ride ")
    age = int(input("Enter Your age "))
    if age < 12:
        print("paid 150 Rs ")
        photo = int (input("If you want photo press 1 if do not want press 0"))
        if photo == 1:
            print("Paid Total  Rs 200")
    elif age <= 18:
        print("Paid Rs 250 ")
        photo = int(input("If you want photo press 1 if do not want press 0"))
        if photo == 1:
            print("Paid Total  Rs 300")
        else:
            print("Paid Total Rs 250 ")
    elif age > 18:
        print("Paid Rs 500 ")
        photo = int(input("If you want photo press 1 if do not want press 0"))
        if photo == 1:
            print("Paid Total  Rs 550")
        else:
            print("Paid Total Rs 500 ")

    else:
        print("Paid Total Rs 150 ")
else:
    print("Can,t Ride ")
