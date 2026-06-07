# अगर सिर्फ error दिखाना हो, तो built-in exceptions (ValueError, TypeError, etc.) काफी हैं। लेकिन custom exceptions का फायदा code को ज्यादा meaningful और maintainable बनाना है।

# eski madadd se hum full control kar sakte hai exception ko
# Custom Exceptions

class NegativeAmountError(Exception):
    """Raised when withdrawal amount is negative"""
    pass


class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance"""
    pass


class Bank:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError(
                "Withdrawal amount cannot be negative"
            )

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance in account"
            )

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


try:
    account = Bank("Gopal Sharma", 5000)

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    else:
        print("Invalid choice")

except NegativeAmountError as e:
    print("NegativeAmountError:", e)

except InsufficientBalanceError as e:
    print("InsufficientBalanceError:", e)

except ValueError as e:
    print("ValueError:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Thank you for using our banking service.")