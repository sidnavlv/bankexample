class AccountHolder:
  def __init__(self, name, dob):
    print("Init called 1")
    self.name = name
    self.dob = dob
    #self.account = account
   
  @staticmethod
  def createAccountHolder() -> any: 
   print("Static/Class method demo")
 
  def __str__(self) -> str:
    return f"\n\nAccount Holder Name: {self.name} \nAccount Holder DOB: {self.dob}\n"
