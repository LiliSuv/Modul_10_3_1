
import time
from random import randint
import threading
class Bank():
    def __init__(self):
        self.balance =0
        self.lock = threading.Lock ()
    def deposit(self):
        for i in range(1,100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            a =randint (50, 500)
            self.balance = self.balance + a
            print (f'Пополнение: {a}. Баланс: {self.balance} ')
            time.sleep (0.001)

    def take(self):
        for i in range (1, 100):
            a =randint(50,500)
            print(f'Запрос на {a} ')
            if a<=self.balance:
                self.balance = self.balance - a
                print(f'Снятие: {a}. Баланс: {self.balance}. ')
            else:
                try:
                    self.lock.acquire ()
                finally:
                    self.lock.release ()
                    print(f'Запрос отклонён, недостаточно средств. ')
            time.sleep (0.001)

bk = Bank()
th1 = threading.Thread (target=Bank.deposit, args=(bk,))
th2 = threading.Thread (target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')