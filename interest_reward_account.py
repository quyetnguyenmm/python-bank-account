from bank_account import BankAccount

class InterestRewardAccount(BankAccount):
    def deposit(this, amount):
        this._balance = this._balance + (amount * 1.05)
        print("Funds have been transferred to this account. 🎉")
        this.getBalance()