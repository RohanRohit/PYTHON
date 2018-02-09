a=float(input(""))
if a >= 1.0 and a<=100000.0:
    print("positive")
elif a == 0:
    print("zero")
elif a < 0:
    print("negative")
else:
    print("enter the range between 0 to 100001")
