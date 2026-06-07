#class
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        # Negative amount check
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")

        # Insufficient balance check
        if self.balance < amount:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully")
        print(f"Remaining Balance: ₹{self.balance}")

try:
    account = Bank(5000)

    amount = int(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Thank you for using our bank service.")