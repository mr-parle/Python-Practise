class atm:
    def __init__(self):

        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = int(input("""enter the number to proceed
            1. Create pin
            2. Check Balance
            3. Deposit
            4. Withdraw
            """))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.check_balance()
        elif user_input == 3:
            self.deposit()
        elif user_input == 4:
            self.withdraw()

    def create_pin(self):
        self.pin = int(input("Enter PIN: "))
        print("PIN Created Sucessfully")

    def check_balance(self):
        temp = int(input("Enter PIN to Proceed"))
        if temp == self.pin:
            print(self.balance)

    def deposit(self):
        temp = int(input("Enter PIN to Proceed"))
        if temp == self.pin:
            amount = int(input("Enter Amount"))
            self.balance += amount
            print("Deposited Sucessfully")

    def withdraw(self):
        temp = int(input("Enter PIN to Proceed"))
        if temp == self.pin:
            amount = int(input("Enter Amount"))
            if amount<=self.balance:
                self.balance -= amount
                print("Withdrawed Sucessfully")



sbi= atm()
sbi.menu()


