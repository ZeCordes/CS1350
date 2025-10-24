class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance
        
        if initial_balance <= 0:
            raise TypeError("Account must be created with a positive balance.")

    def deposit(self, amount):
        if amount <= 0:
            raise TypeError("Must deposit a positive amount of money.")

        self._balance += amount
        
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise TypeError("Must withdraw a positive amount of money.")
        
        if amount > self._balance:
            print("Insufficent Funds.")
            amount = 0 # withdraw nothing
        
        self._balance -= amount
        return self._balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account #{self.account_number} - Owner: {self.owner} - Balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        super().__init__(account_number, owner, initial_balance)
        
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self._balance * self.interest_rate
        self._balance += interest_amount
        
        return interest_amount

    def withdraw(self, amount):
        if self._balance - amount < 100:
            print("Cannot go below $100 minimum")
        else:
            super().withdraw(amount)


# Test your code
if __name__ == "__main__":
    # Regular account
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")
    
    print("\n" + "="*40 + "\n")
    
    # Savings account
    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    
    # Try to go below minimum
    savings.withdraw(950) # Should fail
    savings.withdraw(500) # Should work
    print(f"Final balance: ${savings.balance}")