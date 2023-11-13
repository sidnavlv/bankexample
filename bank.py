import csv
import Account as AC
import AccountHolder as AH
import utility as ut
import mysql.connector

def openAccount() -> AC.Account:  
  accNme = input("Enter Account Holder Name: ")
  dob = ''
  if(ut.validateName(accNme)):
    dob = input("Enter DOB(DD/MM/YYYY): ")
    if(ut.validateDobM2(dob)):
       try:
         a1 = AC.Account(acno=-1,dob=dob,name=accNme,amount=ut.validateAmount(float(input("Enter amount to open account: "))))
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

def load(accs):
  mydb = mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      password="root"
    )

  mycursor = mydb.cursor()
  mycursor.execute("select * from bank.account")

  for row in mycursor:
   print(row)

  with open('account.csv', 'r', newline='') as csvfile:
       rowwreader = csv.reader(csvfile, delimiter=',', quotechar='"')
       for row in rowwreader:
        tmpnac =AC.Account(int(row[0]), row[1], row[2], float(row[3]))
        print(tmpnac)
        accs[int(row[0])]=tmpnac

inp = 0
accs = dict() #{1, tmp}

load(accs)

while inp != 4:
 inp = int(input("\n\nEnter your choice: \n 1 = Open Account \n 2 = Withdraw \n 3 = Deposit \n 4 = Exit\n"))
 
 match inp:
   case 1:
     tmp =  openAccount()
     if(type(tmp) != AC.Account):
      print("Unable to open account")
     else:
      accs[tmp.accountNumber]=tmp
   case 2:
      ano = int(input("\nEnter account no to withdraw from: "))
      amt = float(input("\nEnter amount to withdraw: "))
      if ano in accs.keys():
       if accs[ano].amount-amt < 20 :
         print("Insufficient Funds, Unable to withdraw")
       else:
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
      #for key in accs:
      #  print(accs[key])
      with open('account.csv', 'w', newline='') as csvfile:
       for tmp in accs.values():
           rowwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           rowwriter.writerow([tmp.accountNumber, tmp.accountHolder.name, tmp.accountHolder.dob, tmp.amount])
      print("Exiting...")
      break
   case default:
    print("Invalid Selection")
    
