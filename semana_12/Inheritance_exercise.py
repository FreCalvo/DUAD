# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance`.
#     2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`.

class BankAccount():
    balance = 0

    def add_money(self, amount):
        print('Transaction granted')            
        self.balance += amount
        print(f'Your current balance is: {self.balance}')

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f'Your current balance is: {self.balance}')


class SavingsAccount(BankAccount):
    min_balance = 5000

    def check_account_balance(self):
        if self.balance > self.min_balance:
            print('Withdraw granted')            
        else:
            print('Transaction not allowed, you reached min balance.')
            exit()


bank_account = SavingsAccount()
bank_account.add_money(10000)
bank_account.check_account_balance()
bank_account.withdraw_money(5000)
bank_account.check_account_balance()
bank_account.withdraw_money(1000)



