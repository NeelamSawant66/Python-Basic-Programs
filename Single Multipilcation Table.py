# done

print("Welcome")
num1 = int(input("You Want Table Of: "))
num2 = int(input(f"You Want Table Of {num1} till :"))
print(f"You Have Selected table of {num1} till {num2}")
num =0
while num <= num2:
    print(f"{num1} X {num} = {num1 * num}")
    num +=1