a=int(input("enter the number"))
if a >= 1.0 and a<= 100000.0:
    if a % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")
else:
    print("enter the range between 0 to 100001")
