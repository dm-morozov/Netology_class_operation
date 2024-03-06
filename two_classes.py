class Account:
    """
    Class representing a bank account.

    Args:
        account_number (int): The account number.
        balance (float, optional): The balance of the account. Default is 0.

    Attributes:
        account_number (int): The account number.
        balance (float): The balance of the account.

    """

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств')
            return
        self.balance -= amount


account_1 = Account(42)
print(account_1.balance)
account_1.deposit(50000)
print(account_1.balance)
print('------------------------------')
account_2 = Account(777, 100000)
print(account_2.balance)
account_2.withdraw(150000)
print(account_2.balance)
account_2.withdraw(70000)
print(account_2.balance)


class Bank:
    """
    Class representing a bank.

    Attributes:
        accounts (dict): A dictionary storing the customer accounts.
    """

    def __init__(self):
        self.accounts = {}

    def add_account(self, account):

        if isinstance(account, Account):
            self.accounts[account.account_number] = account
        else:
            print('Некорректное добавление счета')

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print('Счет не найден')

    def find_account(self, account_number):
        return self.accounts.get(account_number, 'Счет не найден')

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        account.withdraw(amount)

green_bank = Bank()
yellow_bank = Bank()

green_bank.add_account(account_1)

print(yellow_bank.accounts)
print(green_bank.accounts)

mega_bank = Bank()
mega_bank.add_account(account_1)
mega_bank.add_account(account_2)

mega_bank.deposit(42, 100)
mega_bank.deposit(777, 200)

mega_bank.withdraw(42, 50)
mega_bank.withdraw(777, 100)

print(mega_bank.accounts)
for number, account in mega_bank.accounts.items():
    print(f'Баланс счета {number} составляет {account.balance}')