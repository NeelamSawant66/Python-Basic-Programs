# print('''Age Calculator''')
# BirthYear= int(input("Enter You Birth Year: "))
# year = 2021 - BirthYear
# print(f"Your Birth Year is {BirthYear} so You Are {year} yrs old"
print('''Age Calculator''')
print("------------------------------------------------------------")
date = 0
print("****Input in  Numbers Only*******")
print("------------------------------------------------------------")
Current_Date = int(input("Enter Current Date: "))
Current_Month = int(input("Enter Current Month: "))
Current_Year = int(input("Enter Current Year: "))
print("------------------------------------------------------------")
BirthDate= int(input("Enter You Birth Date: "))
BirthMonth= int(input("Enter You Birth Month: "))
month = Current_Month - BirthMonth
if BirthMonth == (1,3,5,7 ,8, 10 , 12 ) :
    date = Current_Date - BirthDate
elif BirthMonth == (4,6,9,11) :
    date = Current_Date - BirthDate
else:
    date = Current_Date - BirthDate

BirthYear = int(input("Enter You Birth Year: "))
year = Current_Year - BirthYear
print("------------------------------------------------------------")
print(f"so You Are {year} yrs, {month} months and {date} days old")