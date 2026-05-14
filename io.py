'''output
print("good", end=' ')
print('morning')
#good, morning, welcome etc they are objects.
#end="" print vayesi last ma k hunxa eg, \n, whitespace, tab, etc
#sep, objects lai seperate garna ko lagi use hunxa, default ma space hunxa
print('welcome', 'to', 'python', sep='+')
'''
'''input
# print(5) #5 is a literal
name = input("ur name is? ")
print("hi ", name)
n1= input("enter num1: ")
n2= input("enter num2: ")
add= int(n1) + int(n2)
print("the sum is: ", add)'''

'''operators
a = 2
b = int(input("enter: "))

sum = a + b
diff = a - b
prod = a * b

print("sum:", sum, "diff:", diff, "prod:", prod, sep=", ")
print(a**b)
#a **=b #a = a**b= a powered b 
#print(a)
print(a>b)'''

num = int(input("Enter marks: "))
if num>=60:
    if num>=90:
        print("A+")
    elif num>=80:
        print("A")
    elif num>=70:
        print("B+")
    else:
        print("B")
elif num>=50:
    print("C")
else:
    print("fail")