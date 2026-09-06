files = "records.txt"

print("\n---STUDENT RECORDS---\n")
n = int(input("ENter number of students: "))
try:
    lst = []
    with open(files, "w") as f:
        for i in range(n):
            name = input(f"\nENter name of std{i+1}: ")
            marks = float(input(f"ENter marks of {name}: "))
            try:
                lst.append(marks)
                f.write(f"{name}, {marks} \n") 
            except ValueError:
                print("\nERROR: Invalid input. Please enter a valid number.\n")
        print("\n---RECORD CREATED SUCCESSFULLY---\n")
        try:
            print("\n---STUDENT RECORDS---\n")
            with open(files, "r") as f:
                rec = f.read()
                print(rec)
        except FileNotFoundError:
            print("\nERROR: File not found.\n")
        total = 0
        for i in lst:
            total += i
        avg = total/len(lst)
        print(f"\n Average marks of the students: {avg}. \n")
except ValueError:
    print("\nERROR: Invalid input. Please enter a valid number.\n")
