import threading
import time


class ThreadSafety:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        lock.acquire()
        print("Current thread is ", threading.current_thread().getName())
        print("Current balance is ", self.balance)
        print("Lock acquired by ", threading.current_thread().getName())
        time.sleep(5)
        if self.balance > amount:
            if self.balance > 5000:
                self.balance = self.balance - amount
                print(threading.current_thread().getName(),
                      "has withdrawn the money")
                print("Remaining balance is ", self.balance)
            else:
                print("Can't withdraw")
        else:
            print("Can't withdraw")

        print(threading.current_thread().getName(), "exit")
        lock.release()
        print("Lock released by ", threading.current_thread().getName())
        # print("Balance after transaction by ",
        #       threading.current_thread().getName(), " is ", self.balance)


obj = ThreadSafety(10000)

lock = threading.Lock()

thread1 = threading.Thread(target=obj.withdraw, args=(4000,), name="Thread_1")
thread2 = threading.Thread(target=obj.withdraw, args=(4000,), name="Thread_2")
thread3 = threading.Thread(target=obj.withdraw, args=(4000,), name="Thread_3")
thread4 = threading.Thread(target=obj.withdraw, args=(4000,), name="Thread_4")

thread1.start()
thread2.start()
thread3.start()
thread4.start()
