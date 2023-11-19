import AccountHolder as AH
import accountdao as DAO
import amountopt as AO
class Account:
  #accno=0 #with database auto increment primary key this is not needed
  # def __init__(self, accountHolder, amount) -> None:
  #   print("Init called 2")
  #   self.amount=amount
  #   print(type(self.amount))
  #   self.accountHolder=accountHolder
  #   self.accountNumber=Account.accno
  #   Account.accno+=1
  #   #accountHolder.account=self
  @classmethod
  def getAccountById(cls, id) -> any:
     return DAO.getAccountByAccNo(id)

  def __init__(self, acno, name, dob, amount) -> None:
    print("Init called New")
    self.amount=amount
    self.accountNumber=acno
    self.accountHolder = AH.AccountHolder(name, dob)

  def createAccount(self) -> int:
     return DAO.createAccount(self)

  def deposit(self, amount):
    self.amount = DAO.modifyAmount(self.accountNumber, amount, AO.Opt.ADD)
    print(self)
    
  def withdraw(self, amount):
    self.amount = DAO.modifyAmount(self.accountNumber, amount, AO.Opt.SUB)
    print(self)

  def __str__(self) -> str:
    return f"{self.accountHolder}Account Number: {self.accountNumber}\nAmount: {self.amount}"
