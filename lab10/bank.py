class Account:
    def __init__(self, customer_id, account_nbr):
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance = 0

    def get_customer_id(self):
        return self._customer_id

    def get_account_nbr(self):
        return self._account_nbr

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return (
            f'Account(owner: {self._customer_id}, '
            f'nbr: {self._account_nbr}, '
            f'balance: {self._balance})'
        )

    def __repr__(self):
        return str(self)


class Bank:   
    
    customer_id = 1
    account_id = 1

    def __init__(self) -> None:
        self._customers = {}
        self._accounts = {}
        Bank.customer_id += 1
        Bank.account_id += 1

    
    def add_customer(self,name):
        pass

    
    def get_customer_name(self, customer_id):
        pass

    def get_customer_id(self):
        return self.customer_id
    
    def get_account_id(self):
        return self.account_id







b = Bank()
b2 = Bank()

print(b.get_customer_id())
