#match case of python similar to switch caseof C
n = int(input("Enter a number: "))
match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Other number") #underscore wala is for default as in switch
        