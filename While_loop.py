count = 0
while count <= 5:
    print(count, end=" ")
    count += 1
else:
    print("\nIN else block \n")

#while loop else block control

num = 1
while num <= 6:
    print(num, end=" ")
    num += 1
    if num == 5:
        break
else:
    print("Out of While Loop")
print("\nout of Else block\n")


#while loop control by user

user = int(input("Enter a Number (-2 for quit): "))
while user != -2:
    print(user)
    user = int(input("Enter a Number (-2 for quit): "))

else:
    print("IN else block: ")
print("Out from Loop: \n")



count1 = 0
while True:
    print(count1)
    count1 += 1
    if count1 == 5:
        break
else:
    print("IN else block")
print("\nout of While loop\n")

# Count Total Enter value

total = 0
number = int(input("Enter a Number (0 to Quit)"))
while number != 0:
    total = total + number
    number = int(input("Enter a Number (0 to Quit)"))
print(total)

