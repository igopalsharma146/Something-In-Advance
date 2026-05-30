# thread synchronization
import threading
import time
# Create a lock
lock = threading.Lock()

balance = 200

def deposit(amount,lock):
    global balance
    with lock:
        balance += amount
    print(f"Deposited {amount}, new balance: {balance}")

def withdraw(amount,lock):
    global balance
    with lock:
        if balance >= amount:
            balance -= amount
            print(f"Withdrew {amount}, new balance: {balance}")
        else:
            print(f"Insufficient funds to withdraw {amount}, current balance: {balance}")
# Create threads for deposit and withdraw
thread1 = threading.Thread(target=deposit, args=(100,lock))
thread2 = threading.Thread(target=withdraw, args=(50,lock))
thread3 = threading.Thread(target=withdraw, args=(300,lock))