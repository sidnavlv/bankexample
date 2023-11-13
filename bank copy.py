import utility as ut
import json #javascript object notation

class AccountHolder:
  def __init__(self, name, dob):
    print("Init called 1")
    self.name = name
    self.dob = dob
    #self.account = account
   
  @staticmethod
  def createAccountHolder() -> any: 
    accNme = input("Enter Account Holder Name: ")
    dob = ''
    if(ut.validateName(accNme)):
      dob = input("Enter DOB(DD/MM/YYYY): ")
      if(ut.validateDobM2(dob)):
          return AccountHolder(accNme, dob)
      else:
        print("not valid DOB")  
    else:
      print("not valid Name")  
 
  def __str__(self) -> str:
    return f"\n\nAccount Holder Name: {self.name} \nAccount Holder DOB: {self.dob}\n"

class Account:
  accno=1
  def __init__(self, accountHolder, amount) -> None:
    print("Init called 2")
    self.amount=amount
    print(type(self.amount))
    self.accountHolder=accountHolder
    self.accountNumber=Account.accno
    Account.accno+=1
    #accountHolder.account=self

  def deposit(self, amount):
    self.amount += amount
    print(self)
    
  def withdraw(self, amount):
    self.amount -= amount
    print(self)

  def __str__(self) -> str:
    return f"{self.accountHolder}Account Number: {self.accountNumber}\nAmount: {self.amount}"


def openAccount() -> Account:  
  a1 = Account(AccountHolder.createAccountHolder(), float(input("Enter amount to open account: ")))
  print(a1)
  return a1

inp = 0
accs = dict()
while inp != 4:
 inp = int(input("\n\nEnter your choice: \n 1 = Open Account \n 2 = Withdraw \n 3 = Deposit \n 4 = Exit\n"))
 
 match inp:
   case 1:
     tmp =  openAccount()
     accs[tmp.accountNumber]=tmp
     json_obj = json.dumps(tmp, indent=4, default=lambda obj: obj.__dict__)
     file = open("account.json", "a")
     file.write(json_obj)
     file.close()
   case 2:
      ano = int(input("\nEnter account no to withdraw from: "))
      amt = float(input("\nEnter amount to withdraw: "))
      if ano in accs.keys():
       accs[ano].withdraw(amt) 
      else:
       print("\nAccount not exist")
   case 3:
      try:
        ano = int(input("\nEnter account no to deposit to: "))
        amt = float(input("\nEnter amount to deposit: "))
        accs[ano].deposit(amt)   
      except KeyError:
        print("\nAccount not exist") 
   case 4:
      print("Exiting...")
      break
   case default:
    print("Invalid Selection")
    
