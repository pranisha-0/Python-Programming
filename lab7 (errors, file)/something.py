FILE_NAME = "student_marks.txt"


def create_student_file():
	try:
		number_of_students = int(input("Enter the number of students: "))
		if number_of_students < 1:
			raise ValueError("The number of students must be positive.")

		with open(FILE_NAME, "w") as file:
			for student_number in range(number_of_students):
				name = input(f"Enter name of student {student_number + 1}: ").strip()
				if not name:
					raise ValueError("Student name cannot be empty.")

				marks = float(input(f"Enter marks for {name}: "))
				if marks < 0 or marks > 100:
					raise ValueError("Marks must be between 0 and 100.")

				file.write(f"{name} {marks:g}\n")
	except ValueError as error:
		print(f"Invalid input: {error}")
		return False

	return True


def read_student_file():
	records = []

	try:
		with open(FILE_NAME, "r") as file:
			for line_number, line in enumerate(file, start=1):
				parts = line.split()
				if len(parts) != 2:
					raise ValueError(f"Invalid record on line {line_number}.")

				name, marks_text = parts
				marks = float(marks_text)
				if marks < 0 or marks > 100:
					raise ValueError(f"Invalid marks on line {line_number}.")

				records.append((name, marks))
	except FileNotFoundError:
		print(f"Error: {FILE_NAME} was not found.")
		return
	except ValueError as error:
		print(f"Error: {error}")
		return

	print("\nStudent records:")
	for name, marks in records:
		print(f"{name} {marks:g}")

	if records:
		average = sum(marks for _, marks in records) / len(records)
		print(f"Average marks: {average:.2f}")
	else:
		print("No student records found.")


if create_student_file():
	read_student_file()
