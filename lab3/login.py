user = "pran@123"
pas = "pranisha01"

nam = input("PLEASE ENTER USERNAME: ")
word = input("PLEASE ENTER PASSWORD: ")

if nam == user and word == pas:
    print("LOGIN SUCCESSFUL.")
elif nam == user and word != pas:
    print("INCORRECT PASSWORD.")
else:
    print("USER NOT FOUND.")