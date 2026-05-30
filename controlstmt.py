mark = float(input("Enter ur mark: "))
if mark >= 40:
    print("pass")
    if mark>=90: 
        print("A+")
    elif mark>= 80:
        print("A")
    elif mark>= 70:
        print("B+")
    elif mark >= 60:
        print("B")
    else:
        print("C")
else:
    print("Fail")
    print("Try again...")