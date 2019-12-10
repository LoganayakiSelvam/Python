accno=int(input("enter aacno :"))
ganil=input("enter gmail :")
values='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 
if values in gamil:
 print("valid")
 break
else:
 print("enter valid gamil")
 contine
pswrd=int(input("enter the pswrd :"))
l=len(pswrd)
if l!=6:
 print("pswrd must contanin alteast 6 characters :")
 continue
else:
 print("valid")
 break
mbno=int(input("enter the mbno:")) 
if len(mobno)!=10 or mobno[0]!=9:
 print("enter valid mobile no")
 continue
else: 
 print("mobno:",mobno)
 break
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
 a=int(2000,3000) 
 print("accno:",a)
 balance=9000  
 print("available balance :",balance) 
elif select=="Display":
  print("gmail:",gmail) 
  print("accno:",a) 
  print("balance:",balance)
