roll_num = [1,2,3,4,5]
print (roll_num)
print(roll_num[0],roll_num[3])

names = ["Miad", "Bhuiyan"]
print(names)

mix_list = [190,"miad",10.23]
print(mix_list)
print(mix_list[1])

duplicate = [1,2,3,4,1,2]
print(duplicate)
print(len(duplicate))
print(duplicate[1:5])
print(duplicate[0:6:2])

no=[-90,-230,90,300,1,34]
no.sort()#first sort than print rather than show in output none
print(no)
no.append(345)
print(no)
no.insert(2,3567)
print(no)
no.extend([45,34,56])
print(no)
no[0] = 3456
print(no)
no[0:3] = [2,4,6,7]
print(no)
no.remove(56)
print(no)
no.pop()
print(no)
no.pop(3)
print(no)
print(no.count(300))