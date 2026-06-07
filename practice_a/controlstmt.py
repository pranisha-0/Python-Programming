'''if else, nested if else, elif
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
    print("Try again...")'''

#for lists, 
names = ['pranisha', 'pranesh', 'puja', 'pratiksha']
for hehe in names:
    print(hehe)
'''yo mathi ko code ma k hunxa vane, 
* "hehe" lai iteration value assign garxa
* first ma hehe = names[0] = pranisha hunxa 
* ani hehe = names[1] = pranesh hunxa
* tesari nai sabai statement haru execute hunxa ani print garxa'''

#for strings
nam = "pran"
for x in nam:
    print(x)
'''* x = nam[0] = p
* x = nam[1] = r'''

value = range(1,6)
for i in value:
    print(i)