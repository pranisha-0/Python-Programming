with open("rec.txt", "w") as f:
    for i in range(2):
        nam = input(f"Enter your name: ")
        rollno = input(f"enter rollno. : ")
        college = input(f"enter college name: ")
        f.write(f"{nam}, {rollno}, {college}. \n")


with open("rec.txt", "r") as f:
    print("\n---RECORD---\n")
    for l in f:
        print(l, end="\n")

