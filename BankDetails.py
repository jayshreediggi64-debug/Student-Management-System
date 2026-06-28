from abc import ABC, abstractmethod

# ---------------- Parent Class ----------------
class Bank(ABC):
    bank_name = "State Bank of India"
    branch = "Patiala"

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def __init__(self, holder_name, account_number, balance):

        if not holder_name.replace(" ", "").isalpha():
            raise ValueError("Invalid Account Holder Name!")

        if not (account_number.isdigit() and len(account_number) == 10):
            raise ValueError("Account Number must contain exactly 10 digits!")

        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
        print(f"₹{amount} Deposited Successfully")
        return self

    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"₹{amount} Withdrawn Successfully")
        else:
            print("Insufficient Balance")
        return self

    def display(self):
        print("\n------ ACCOUNT DETAILS ------")
        print("Bank Name      :", Bank.bank_name)
        print("Branch         :", Bank.branch)
        print("Holder Name    :", self.holder_name)
        print("Account Number :", self.account_number)
        print("Balance        :", self.get_balance())

    @abstractmethod
    def add_interest(self):
        pass


# ---------------- Saving Account ----------------
class SavingAccount(Bank):

    def __init__(self, holder_name, account_number, balance):
        super().__init__(holder_name, account_number, balance)   # Constructor Chaining

    def add_interest(self):
        interest = self.get_balance() * 0.05
        self.set_balance(self.get_balance() + interest)
        print("5% Interest Added:", interest)


# ---------------- Salary Account ----------------
class SalaryAccount(Bank):

    def __init__(self, holder_name, account_number, balance):
        super().__init__(holder_name, account_number, balance)   # Constructor Chaining

    def add_interest(self):
        pass

    def deposit(self, amount):
        if amount <= 20000:
            self.set_balance(self.get_balance() + amount)
            print("Deposit Successful")
        else:
            print("Deposit Limit is ₹20000")
        return self

    def withdraw(self, amount):
        if amount < 10000:
            print("Minimum Withdrawal Amount is ₹10000")
        elif amount > self.get_balance():
            print("Insufficient Balance")
        else:
            self.set_balance(self.get_balance() - amount)
            print("Withdrawal Successful")
        return self


# ---------------- Main Program ----------------

print("===== Saving Account =====")
s1 = SavingAccount("Jerry", "1234567890", 50000)

s1.deposit(5000).withdraw(3000)

s1.add_interest()
s1.display()


print("\n===== Salary Account =====")
sal = SalaryAccount("Jerry", "9876543210", 40000)

sal.deposit(15000).withdraw(12000)

sal.display()

Bank.change_bank_name("Punjab National Bank")

print("\nAfter Changing Bank Name")
s1.display()