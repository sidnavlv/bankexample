import AccountHolder as AH
class Account:
  accno=0
  # def __init__(self, accountHolder, amount) -> None:
  #   print("Init called 2")
  #   self.amount=amount
  #   print(type(self.amount))
  #   self.accountHolder=accountHolder
  #   self.accountNumber=Account.accno
  #   Account.accno+=1
  #   #accountHolder.account=self

  def __init__(self, acno, name, dob, amount) -> None:
    print("Init called 3")
    self.amount=amount
    self.accountNumber=acno
    if acno == -1:
      Account.accno+=1
      
    else:
      Account.accno = acno

    self.accountNumber=Account.accno
    self.accountHolder = AH.AccountHolder(name, dob)

  def deposit(self, amount):
    self.amount += amount
    print(self)
    
  def withdraw(self, amount):
    self.amount -= amount
    
    print(self)

  def __str__(self) -> str:
    return f"{self.accountHolder}Account Number: {self.accountNumber}\nAmount: {self.amount}"
