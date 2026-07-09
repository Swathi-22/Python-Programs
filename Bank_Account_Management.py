
class BankAccount:
    def __init__(self):
        pass

    def deposit(self,dep):
        self.dep = dep
        return self.dep
    
    def withdraw(self,wid):
        self.wid = wid
        return self.wid

    def balance(self,ini_bal,dep_amt,wid):
        self.ini_bal = ini_bal
        self.dep_amt = dep_amt
        self.wid = wid
        return ini_bal + dep_amt - wid
        

ini_bal = int(input("Initial Balance : "))
dep_amt = int(input("Deposit Amount : "))
wid_amt = int(input("Withdraw Amount : "))

ba = BankAccount()
print("\t")
print(f"Amount Deposited : {ba.deposit(dep_amt)}")
print(f"Amount Withdrawn : {ba.withdraw(wid_amt)}")
if ba.balance(ini_bal,dep_amt,wid_amt) > 0 :
    print(f"Current Balance : {ba.balance(ini_bal,dep_amt,wid_amt)}")
else:
    print("Money can't withdraw due to insufficient balance.")
