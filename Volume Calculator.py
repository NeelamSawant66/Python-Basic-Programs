print('''Welcome to Volume Calculator 
1. Cube
2. Rectangle
3. Sphere
4. Triangle''')
def volume() :
    option = int(input("Select Any One Option : "))
    if option==1:
        print("Volume Of Cube")
        side = float(input("Enter Side of Cube : "))
        cube = side * side * side
        print(f"The Volume of Cube is {cube} cube cm ")
        ask()
    elif option==2:
        print("Volume Of Rectangle")
        length= float(input("Enter The Length Of Rectangle:"))
        breadth = float(input("Enter The Breadth Of Rectangle : "))
        width = float(input("Enter The Width Of Rectangle : "))
        rectangle = length * breadth * width
        print(f"The Volume Of Rectangle is {rectangle}cube cm")
        ask()
    elif option==3:
        print("Volume Of Sphere")
        radius=float(input("Enter Radius Of Sphere :"))
        sphere = 4 / 3 * 3.14 * radius * radius
        print(f"The Volume Of Sphere Is {sphere}cube cm")
        ask()
    elif option==4:
        print("Volume Of Triangle")
        base=float(input("Enter The Base Of Triangle"))
        length = float(input("Enter The length Of Triangle : "))
        height =float(input("Enter The height Of Triangle"))
        triangle= 2/ base* height * length
        print(f"The Volume Of Triangle is {triangle} cube cm")
        ask()
    else:
        print("Invalid Input!!! ,Try Again")
        volume()


volume()
def ask():
    print("1. Contiune"
          "2. Exit")
    option = int(input("Do You Want to find any other Volume calculations"))
    if option ==1:
        volume()
    elif option==2 :
        print("Thank You!!!")
    else:
        print("Invalid Input!!!, try Again")
        ask()

ask()