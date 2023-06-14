import array as arr
a = arr.array('i',[1,2,3])
print("Array before inserting: ",end = " ")
for i in (a):
    print(i,end = " ")
print()

#insert array
a.insert(1,4)

print("Array after inserting : ",end = " ")
for i in (a):
    print(i,end = " ")
print()

#insert array
a.insert(2,8)

print("Array after inserting : ",end = " ")
for i in (a):
    print(i,end = " ")
print()

#complaxity of this program is O(n)