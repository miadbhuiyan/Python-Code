weight = input("Enter weight in kg : ")
height = input("Enter height in Meter: ")

bmi = int(weight)/float(height) ** 2
if bmi<16.0:
    print("UnderWeight(Severe thinness)")
elif bmi <= 18.4:
    print("UnderWeight(Modarate thinness)")
elif bmi <= 21.9:
    print("UnderWeight(Mild thinness")
elif bmi <= 24.9:
    print("Normal Range")
elif bmi <= 29.9:
    print("OverWeight(Pre-obese)")
elif bmi <= 34.9:
    print("Obese(class1")
elif bmi <= 39.9:
    print("Obese(class2")
elif bmi > 40.0:
    print("Obese(class3)")
else:
    print("end")


