import random
user_choice = int(input("Enter your choice: Type 0 for Rock,1 for Paper,2 for scissors : "))
computer_choice = random.randint(0,2)
print("Computer Choise")
print(computer_choice)
if computer_choice == user_choice:
    print("It's Draw")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
elif user_choice == 0 and computer_choice ==2:
    print("you Win")
elif computer_choice>user_choice:
    print("You Lose")
elif user_choice>computer_choice:
    print("You Win")
