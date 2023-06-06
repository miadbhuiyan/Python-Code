height = int(input("Whats your height in feet : "))
if height >= 3:
    print("You can ride ")
    age = int(input("What your age "))
    if age < 12:
        print("Pay 150 taka ")
    elif age <= 18:
        print("Pay 250 taka ")
    else:
        print("pay 500 Taka ")
else:
    print("cann,t ride")
print("Bye")