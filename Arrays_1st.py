# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as student


# creating an array with integer type
a = student.array('i',[1,2,3])

# printing original array
print("The new creating array is : ", end =" ")
for j in range(0,3):
    print(a[j], end=" ")
print("\nPrint array")

# creating an array with float type
b = student.array('d',[2.3,3.4,3.5])
print("the new creating array is : ", end = " ")
for k in range(0,3):
    print(b[k],end = " ")

#Time complexity of this code is O(n)
