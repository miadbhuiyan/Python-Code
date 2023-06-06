#text = "Welcome to Miad lectures "
#text_splitted = text.split()
#print(text_splitted)

import random
names = input("Enter everbody's name separated by comma : ")
names_list = names.split(",")
#print(names_list)
length = len(names_list)
random_choice = random.randint(0,length-1)
print (f"{names_list[random_choice]} will pay the bill")

