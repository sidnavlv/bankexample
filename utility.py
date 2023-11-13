from datetime import date
from datetime import datetime
def validateName(accName) -> bool:  

    isValid = True

    for char in accName:
    # print(char)
     if(char.isdigit() or (char in ["~","!","@","$"])):
      #print(f"-------------------------------> {char}")
      isValid = False
    
    return isValid

def validateDob(dob) -> bool:

    date_components = dob.split('/')
    day, month, year = [int(item) for item in date_components]
    try:
        d = date(year, month, day)
    except:
       return False
    
    return True

def validateDobM2(dob) -> bool:
    try:
        datetime.strptime(dob, "%d/%m/%Y")
    except:
       return False
    
    return True

def validateAmount(amount) -> float:
 if(amount >=100 ):
   return amount
 else:
   raise Exception("Sorry, amount is below 100")
