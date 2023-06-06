set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 ={2,3,7,10,98}
print(set1.issubset(set2))
print(set1.issuperset(set2))

print(set1.symmetric_difference(set2))
print(set1 ^ set2 ^ set3)

print(set1.union(set2,set3))
print(set1 | set2 | set3)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.intersection_update(set2))
print(set1 - set2)


print(set1.union((11,12)))

set2.update([98,78])
print(set2)
print(set1.intersection_update(set2))



print(set1.difference(set2,set3))


set7 = {1,2,3}
set8 = {4,5,6}
print(set7.isdisjoint(set8))
