#Control statement break
list1 = ["hi","hello","welcome"]
names = ["Mid","small","Large"]
for item in list1:
    for name in names:
        print(item,name)
        if item == "welcome" and name == "Mid":
            break
        print("LOOK AT THE IF CODITION TO UNDERSTAND BREAK")
    print("out of inner for loop")
print("out of for loop\n ")


#Control statement continue
list2 = ["hi","hello","welcome"]
names1 = ["Mid","small","Large"]
for i in list2:
    for j in names1:
        print(i,j)
        if i == "hi" and j == "Large":
            continue
        print("LOOK AT THE IF CODITION TO UNDERSTAND BREAK")
    print("out of inner for loop")
print("out of for loop ")


#Control statement continue
for i in range(1,11):
    pass#empty loop