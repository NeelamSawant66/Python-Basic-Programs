import math
print('''Welcome !!!
1.Square
2. Cube
3. Square Root
3. Cube Root''')
def work():
    option =int(input('Select Any One Option : '))
    if option==1:
        square = float(input('Enter value for calculating square: '))
        ans = square*square
        print(f"The Square of {square} is {ans}")
    elif option == 2:
        cube =float(input("Enter value for Calculating cube: "))
        ans = cube*cube*cube
        print(f"The Square of {cube} is {ans}")
    elif option==3:
        SqRoot = float(input('Enter value for calculating Square Root: '))
        ans = math.sqrt(SqRoot)
        print(f"The Square root of {SqRoot} is {ans}")
    elif option==4:
        CuRoot = float(input("Enter the value for calculating Cube Root : "))
        ans =