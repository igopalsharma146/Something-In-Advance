# atm by oops concept
class Atm:
    def __init__(self):
        self.pin = None
        self.balance = 0
        # print("address of the object 'id':", id(self))
        self.menu()
    
    def menu(self):
        # print("address of the object 'id':", id(self))
        user_input = input(""""
        Hello! Welcome to the ATM Machine, How would you like to proceed?
        1. Enter 1 to create a new pin
        2. Enter 2 to Deposit
        3. Enter 3 to Withdraw
        4. Enter 4 to Check Balance
        5. Enter 5 to Exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid input. Please try again.")
            self.menu()

    def create_pin(self):
        self.pin = input("Enter a new 4-digit pin: ")
        print("Pin created successfully!")
        self.menu()

    def deposit(self):
        if self.pin is None:
            print("Please create a pin first.")
            self.menu()
        else:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"Amount deposited successfully! Current balance: {self.balance}")
            self.menu()

    def withdraw(self):
        if self.pin is None:
            print("Please create a pin first.")
            self.menu()
        else:
            temp=input("Enter your pin: ")
            if temp != self.pin:
                print("Incorrect pin. Please try again.")
                self.menu()
                return
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Amount withdrawn successfully! Current balance: {self.balance}")
            self.menu()

    def check_balance(self):
        if self.pin is None:
            print("Please create a pin first.")
            self.menu()
        else:
            temp=input("Enter your pin: ")
            if temp != self.pin:
                print("Incorrect pin. Please try again.")
                self.menu()
                return
            print(f"Your current balance is: {self.balance}")
            self.menu()
atm = Atm()
# print("address of the object 'atm':", id(atm))

#ham jante hai ki python me sab kuch object hota hai, to yaha self ka matlab hai ki ham jis object ke sath kaam kar rahe hai uska reference, aur jab ham self.pin ya self.balance likhte hai to ham us object ke pin aur balance attributes ko access kar rahe hai. Isliye jab ham self.pin = None likhte hai to ham us object ke pin attribute ko None set kar rahe hai, aur jab ham self.balance = 0 likhte hai to ham us object ke balance attribute ko 0 set kar rahe hai. 
#or hum yah check bhi kar sakte h ki self ka address aur atm ka address same hai ya nahi, jisse hume pata chalega ki self actually atm object ko refer kar raha hai.