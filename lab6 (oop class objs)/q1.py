class BankAccount:
    def __init__(self, acc_num, acc_holder, balance):
        self.a_n = acc_num
        self.a_h = acc_holder
        self.bal = balance
    def deposit(self, amt):
        self.bal += amt
        return (f"{amt} DEPOSITED.")
    def withdraw(self, amt):
        if amt > self.bal:
            print("Insufficient balance")
        else: 
            self.bal -= amt
            return (f"{amt} WITHDRAWN.")
    def disp_balance(self):
        return (f"CURRENT BALANCE: {self.bal}")

p1 = BankAccount(12422, "Pran", 10000)
print(p1.deposit(3000))
print(p1.disp_balance())
print(p1.withdraw(5000))
print(p1.disp_balance())

