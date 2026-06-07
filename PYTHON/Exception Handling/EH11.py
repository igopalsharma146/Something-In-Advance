# Custom Exceptions

class NegativeAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass


class Bank:
    def __init__(self, balance):
        self.balance = balance

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
        print(f"₹{amount} withdrawn successfully")
        print(f"Remaining Balance: ₹{self.balance}")


try:
    account = Bank(5000)

    amount = int(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except NegativeAmountError as e:
    print("NegativeAmountError:", e)

except InsufficientBalanceError as e:
    print("InsufficientBalanceError:", e)

except ValueError:
    print("Please enter a valid number.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Thank you for using our bank service.")
    

# Custom Exceptions

# class NegativeAmountError(Exception):
#     def __init__(self, message):
#         print(message)

# class InsufficientBalanceError(Exception):
#     def __init__(self, message):
#         print(message)


# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):

#         if amount < 0:
#             raise NegativeAmountError(
#                 "Withdrawal amount cannot be negative"
#             )

#         if amount > self.balance:
#             raise InsufficientBalanceError(
#                 "Insufficient balance in account"
#             )

#         self.balance -= amount
#         print(f"₹{amount} withdrawn successfully")
#         print(f"Remaining Balance: ₹{self.balance}")


# try:
#     account = Bank(5000)

#     amount = int(input("Enter withdrawal amount: "))
#     account.withdraw(amount)

# except NegativeAmountError as e:
#     pass

# except InsufficientBalanceError as e:
#     pass

# except ValueError:
#     print("Please enter a valid number.")

# except Exception as e:
#     print("Unexpected Error:", e)

# finally:
#     print("Thank you for using our bank service.")