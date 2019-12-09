def accno():
  try:
    no=int(intput("Enter the accno:"))
    return no
  except TypeError:
    print("enter valid accno")
    accno()

def name():
  na=input("Enter the name:")
  for i in na:
    if ord(i) not in range(65,123):
      print("Enter the correct name:") 
      name()
  return na

def pas():
  try:
    pword=int(input("Enter the password:"))
    return pword
  except TypeError:
    if len(data['ps'])<8:
     print("Enter the correct password which contains 8 characters")
  pas()








choice=input("enter choice(Create new account/Login to existing account) :")
if choice=="Create new account":
 try:
  accno=int(intput("Enter the accno:"))
 except ValueError:
  print('\nType an integer not characters or symbols\nTry again\n')
elif choice=="Login to existing account":
 account_no=accno()
 user_name=name()
 password=pas()
  if account_no in d and user_name in d and pasword in d:
    select()
else:
 print('\nInvalid choice choices are between(1-2)\n')
    

firstname=input("first name:")
lastname=input("last name:")
create_username=input("username:")
create_password=input("password:")
accno4=int(input("accno:")) 
def select():
 select=input("enter select(Withdrawl/Deposit/BalanceEnquiry/Display) :")
 if select=="Withdrawl":
  amount=int(input("enter amount value: "))
  minamount=2000
  if amount<=minamount: 
   print("your balance is less")
  else:
   print("Withdrawl is completed successfully")
 elif select=="Deposit":
  amount=int(input("enter amount value: "))
  minamount=10000
  if amount<=minamount:
   print("please deposit above than your minamout")
  else:
   print("your amount is successfully deposited")
 elif select=="BalanceEnquiry":
  print("balance details")
 elif select=="Display":
  print(firstname+" "+lastname,'\n',create_username,'\n',create_password,)
 else:
  print("invalid")

  

