#done

num = int(input("Enter A Number:- "))
if num>1:
    for i in range(2,num):
        if (num % i)==0 :
            print(f"{num} is not a prime number")
            print(f"{i} times {num//i} is {num}")
            break6
        else:
            print(f"{num} is a prime Number")
else:
    print(f"{num} is not a prime Number")
