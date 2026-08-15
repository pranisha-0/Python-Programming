class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.eid = emp_id
        self.n = name
        self.bs = basic_salary
    def input(self):
        self.eid = int(input("Enter employee id: "))
        self.n = input("ENter name: ")
        self.bs = float(input("Enter basic salary: "))
    def net_salary(self):
        self.net_salary = (self.bs + (20/100) * self.bs)
    def display(self):
        return f"Employee ID: {self.eid} \nEmployee name: {self.n} \nBasic salary: Rs.{self.bs} \nNet salary after 20% bonus: Rs.{self.net_salary}"

e1 = Employee(0, "", 0)
#e2 = Employee(0, "", 0)
e1.input()
#e2.input()
e1.net_salary()
print(e1.display())
#e2.display()