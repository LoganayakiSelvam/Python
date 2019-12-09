def name():
  name=input("Enter the name:")
  for i in name:
    if ord(i) not in range(45,134):
      print("Enter the correct name:") 
      name()
  return name


def accno():
  try:
    accno=int(intput("Enter the accno:"))
    return accno
  except TypeError:
    print("accno must contain only integer values")
    accno()



def pas():
  try:
    password=int(input("Enter the password:"))
    return password
  except TypeError:
    if len('pas')<8:
     print("Enter the correct password which contains 8 characters")
    pas()








choice=input("enter choice(Create new account/Login to existing account) :")
if choice=="Create new account":
 try:
  accno=int(input("Enter the accno:"))
 except ValueError:
  print('\nType an integer not characters or symbols\nTry again\n')
elif choice=="Login to existing account":
 user_name=name() 
 account_no=accno()
 password=pas()
 if account_no in d and user_name in d and pasword in d:
  select()
else:
 print("invalid select only Create new account or Login to existing account")
    


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
  firstname=input("first name:")
  lastname=input("last name:")
  create_username=input("username:")
  create_password=input("password:")
  accno4=int(input("accno:")) 
  print(firstname+" "+lastname,'\n',create_username,'\n',create_password,)
 else:
  print("invalid")

  

