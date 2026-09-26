#wap to print nthterm of fibonacci series
def fibo(n):
    if n== 0 or n==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter term num: "))
if n<0:
    print("Invalid input")
else:
    print(f"The value of {n}th term is {fibo(n)}")