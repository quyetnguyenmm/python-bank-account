from balance_exception import BalanceException
from interest_reward_account import InterestRewardAccount

class SavingAccount(InterestRewardAccount):
    def __init__(this, accountName, initialAmount):
        super().__init__(accountName, initialAmount)
        this.__fee = 5

    def withdraw(this, amount):
        try:
            total = amount + this.__fee
            this.checkViableTransaction(total)
            this._balance = this._balance - total
            print("The withdrawal transaction was successful. 🎉")
            this.getBalance()
        except BalanceException as error:
            print(f"The withdrawal transaction failed:\n{error}")