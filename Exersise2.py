#Pizza Order program
size = input("What size of pizza do you want(s/m/l) ?")
bill = 0
if size == "s" or size == "S":
    bill += 100
elif size =="m" or size == "M":
    bill += 200
else:
    bill += 300

add_pepperoni = input("Do you want pepporoni(y/n)")
if add_pepperoni == "y" or add_pepperoni =="Y":
    if size == "s" or size == "S":
     bill += 30

if add_pepperoni == "y" or add_pepperoni =="Y":
    if size =="m" or size == "M":
     bill += 50

elif add_pepperoni == "n" or add_pepperoni =="N":
    bill = bill


extra_cheese = input("Do you want Extra cheese(y/n)?")
if extra_cheese == "y" or extra_cheese  == "Y":
    bill += 20
else:
    bill = bill
print(f"Your Final bill is {bill}")





