print('''Welcome to Area Calculater 
1. Square
2. Rectangle
3. Circle
4. Triangle''')
def area() :
    option = int(input("Select Any One Option : "))
    if option==1:
        print("Area Of Square")
        side = float(input("Enter Side of Sqaure : "))
        square = side * side
        print(f"The Area of Square is {square}sqcm ")
        ask()
    elif option==2:
        print("Area Of Rectangle")
        length= float(input("Enter The Length Of Rectangle:"))
        breadth = float(input("Enter The Breadth Of Rectangle : "))
        rectangle = length * breadth
        print(f"The Area Of Rectangle is {rectangle}sqcm")
        ask()
    elif option==3:
        print("Area Of Circle")
        radius=float(input("Enter Radius Of Circle :"))
        circle = 3.14* radius*radius
        print(f"The Area Of Circle Is {circle}sqcm")
        ask()
    elif option==4:
        print("Area Of Triangle")
        base=float(input("Enter The Base Of Triangle"))
        height =float(input("Enter The height Of Triangle"))
        triangle= 2/ base* height
        print(f"The Area Of Triangle is {triangle} sqcm")
        ask()
    else:
        print("Invalid Input!!! ,Try Again")
        area()

area()
def ask():
    print("1. Contiune"
          "2. Exit")
    option = int(input("Do You Want to find any other area calculations"))
    if option ==1:
        area()
    elif option==2 :
        print("Thank You!!!")
    else:
        print("Invalid Input!!!, try Again")
        ask()

ask()