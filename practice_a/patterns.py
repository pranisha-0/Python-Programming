'''#10 ota star
print("* "*10)
print("\n")

'''#star box
'''star box
for i in range(0, 5):
    print("* "*5)
print("\n")'''

#left triangle
for i in range (0, 6):
    print("* "*i)

#left upside down triangle
for i in range (6, 0, -1):
    print("* "*i)

#right triangle
for i in range(0, 6):
    print(" "*(6-i)+"*"*i)

#pyramid
for i in range(0, 5):
    print(" "*(5-i)+"* "*(i))

#upside down pyramid
for i in range(5, 0, -1):
    print(" "*(5-i)+"* "*(i))

#diamond
for i in range(5, 0, -1):
    print(" "*(5-i)+"* "*(i))
for i in range(0, 5):
    print(" "*(5-i)+"* "*(i))