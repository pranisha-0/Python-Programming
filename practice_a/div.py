mrk = float(input("Enter marks: "))
if mrk >=0 and mrk <= 100:
    if mrk>= 80:
        print("Distinction")
    else:
        if mrk >= 60:
            print("1st division")
        else:
            if mrk>= 40:
                print("2nd division")
            else:
                print("Fail")
else:
    print("Invalid marks. Try again...")
    