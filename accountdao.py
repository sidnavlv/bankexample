import mysql.connector
import Account as AC
import AccountHolder as AH
import amountopt as AO

mydb = mysql.connector.connect(
      host="localhost",
      port="3306",
      user="root",
      password="root"
)

def getAccountByAccNo(id) -> any:
      mycursor = mydb.cursor()
      mycursor.execute(f"select * from bank.account where accno = {id}")
      acc = None
      for row in mycursor:
        acc = AC.Account(acno=row[1], amount=row[2], dob=row[3], name=row[0])
      mycursor.close()
      return acc
    
def modifyAmount(id, amount, addorsub) -> float:
    mycursor = mydb.cursor()
    if addorsub == AO.Opt.ADD:
      mycursor.execute(f"update bank.account SET amount = (amount+{amount}) where accno = {id}")
    else:
      mycursor.execute(f"update bank.account SET amount = (amount-{amount}) where accno = {id}")
    mydb.commit()
    mycursor.close()
    return getAccountByAccNo(id).amount

def createAccount(account) -> int:
    print("----------------------> CA")
    mycursor = mydb.cursor()
    fdt = account.accountHolder.dob.strftime("%Y/%m/%d")
    mycursor.execute(f"insert into bank.account (accname, dob, amount) values('{account.accountHolder.name}', '{fdt}',{account.amount})")
   
    mydb.commit()
    id = mycursor.lastrowid
    mycursor.close()
    return id