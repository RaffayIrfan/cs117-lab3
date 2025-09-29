
a= int(input("Enter First Number:"))
b= int(input("Enter Second Number:"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b  

def mul(a,b):
    return a*b  

def div(a,b):
    return a/b

def is_even(a):
    if a%2==0:
        return True
    else:
        return False

def percent(a,b):
    return (a/b)*100

loop=True

while loop:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Is Even")
    print("6.Percentage")
    print("7.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Addition is:",add(a,b))
    elif choice==2:
        print("Subtraction is:",sub(a,b))
    elif choice==3:
        print("Multiplication is:",mul(a,b))
    elif choice==4:
        print("Division is:",div(a,b))
    elif choice==5:
        if is_even(a):
            print(a,"is Even")
        else:
            print(a,"is Odd")
        if is_even(b):
            print(b,"is Even")
        else:
            print(b,"is Odd")
    elif choice==6:
        print("Percentage of",a,"over",b,"is:",percent(a,b),"%")
    elif choice==7:
        loop=False
    else:
        print("Invalid Input")