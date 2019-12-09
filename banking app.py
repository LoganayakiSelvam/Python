firstname=input("first name:")
lastname=input("last name:")
create_username=input("username:")
create_password=input("password:")
accno4=int(input("accno:")) 
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
