n = int(input("Enter a number: "))
m = n
s= 0
while n>0:
    r = n%10
    n = n//10
    s = s*10 + r

if s == m:
    print(f"{m} is a palindrome.")
else:
    print(f"{m} isn't a palindrome. ")