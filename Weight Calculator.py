#done

print(''' Welcome To Weight Calculator

 1. Pounds To Kilogram
 2. Kilogram To Pounds''')
def weight():
num = int(input('Select Any One Option: '))
if num ==1:
    weight1= float(input("Enter Weight in Pounds: "))
    result1 = weight1 * 0.45
    print(f"{weight1}lbs = {result1}kg")
elif num ==2:
    weight2= float(input("Enter Weight in Kilograms: "))
    result2 = weight2 / 0.45
    print(f"{weight2}kg = {result2}lbs")
        else:
        print("Invaild Input, Try Again !!!")
        weight()
weight()
