#import csv
import Account as AC
import utility as ut
import datetime

def openAccount() -> AC.Account:  
  accNme = input("Enter Account Holder Name: ")
  dob = ''
  if(ut.validateName(accNme)):
    dob = input("Enter DOB(DD/MM/YYYY): ")
    if(ut.validateDobM2(dob)):
       dt = datetime.datetime.strptime(dob,"%d/%m/%Y")
       try:
         a1 = AC.Account(acno=-1,dob=dt,name=accNme,amount=ut.validateAmount(float(input("Enter amount to open account: "))))
         a1.accountNumber = a1.createAccount()
         print(a1)
         return a1
       except Exception as x:
          print(x)  
          return None
    else:
      print("not valid DOB")  
  else:
    print("not valid Name")  
  return None

#with database and no cache we done need to load all accounts, therefore commenting them.
# def load(accs):
# #In memory cache with no eviction 
#   with open('account.csv', 'r', newline='') as csvfile:
#        rowwreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#        for row in rowwreader:
#         tmpnac =AC.Account(int(row[0]), row[1], row[2], float(row[3]))
#         print(tmpnac)
#         accs[int(row[0])]=tmpnac

inp = 0
#accs = dict() #{1, tmp}

#load(accs)

while inp != 4:
 inp = int(input("\n\nEnter your choice: \n 1 = Open Account \n 2 = Withdraw \n 3 = Deposit \n 4 = Exit\n"))
 
 match inp:
   case 1:
     tmp =  openAccount()
     if(type(tmp) != AC.Account):
      print("Unable to open account")
     else:
      pass
   case 2:
      ano = int(input("\nEnter account no to withdraw from: "))
      amt = float(input("\nEnter amount to withdraw: "))

      acc = AC.Account.getAccountById(ano) #classmethod onlhy works with class name . method name
      #print(acc)
      if acc is not None:
       if acc.amount-amt < 20 :
         print("Insufficient Funds, Unable to withdraw")
       else:
         acc.withdraw(amt) 
      else:
       print("\nAccount not exist")
   case 3:
        ano = int(input("\nEnter account no to deposit to: "))
        amt = float(input("\nEnter amount to deposit: "))
        acc = AC.Account.getAccountById(ano)
        if acc is not None:
          acc.deposit(amt)   
        else:
          print("\nAccount not exist") 
   case 4:
      #for key in accs:
      #  print(accs[key])
      # with open('account.csv', 'w', newline='') as csvfile:
      #  for tmp in accs.values():
      #      rowwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      #      rowwriter.writerow([tmp.accountNumber, tmp.accountHolder.name, tmp.accountHolder.dob, tmp.amount])
      print("Exiting...")
      break
   case default:
    print("Invalid Selection")
    
