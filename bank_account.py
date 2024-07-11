from balance_exception import BalanceException

class BankAccount:
    def __init__(this, accountName, initialAmount):
        this._name = accountName
        this._balance = initialAmount
        print(f"Account '{this._name}' is created.")
        print(f"Available balance = ${this._balance:.2f}\n")
        print("- - - - - - - - - - - - - -")

    def getBalance(this):
        print(f"Account '{this._name}' balance = ${this._balance:.2f}\n")
    
    def deposit(this, amount):
        this._balance = this._balance + amount
        print("Funds have been transferred to this account. 🎉")
        this.getBalance()
    
    def checkViableTransaction(this, amount):
        if this._balance <= amount:
            raise BalanceException("Your balance is not sufficient for this transaction.")
        else:
            return
    
    def withdraw(this, amount):
        try:
            this.checkViableTransaction(amount)
            this._balance = this._balance - amount
            print("The withdrawal transaction was successful. 🎉")
            this.getBalance()
        except BalanceException as error:
            print(f"The withdrawal transaction failed:\n{error}")
    
    def transfer(this, account, amount):
        try:
            print("Transfering ... 🚀")
            this.checkViableTransaction(amount)
            this.withdraw(amount)
            account.deposit(amount)
            print("The transfer transaction was successful. 🎉")
            print("- - - - - - - - - - - - - -")
        except BalanceException as error:
            print(f"The transaction failed:\n{error}")