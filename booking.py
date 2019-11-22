name=input("enter name: ")
location=input("enter location: ")
print(name)
print(location)
source=int(input("enter source: "))
destination=int(input("enter destination: "))
x=destination-source
print(x)
select=input("Enter select(bike/car/premium): ")
if select=="bike":
 km=x*5
elif select=="car":
 km=x*10
elif select=="premium":
 km=x*20
print(km)







n=int(input("enter number: "))
for i in range(0,n,2):
  for j in range(0,n-i-1):
    print(end=" ")
  for j in range(i+1):
    print("*",end=" ")
  print()
for i in range(n-1,0,-2):
  for j in range(0,n-i+1):
    print(end=" ")
  for j in range(i-1):
    print("*",end=" ")
  print()

  
  
  
  
  
  
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
  

