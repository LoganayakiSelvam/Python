name=input("enter name: ")
location=input("enter location: ")
print(name)
print(location)
source=int(input("enter source: "))
destination=int(input("enter destination: "))
if source==0 and destination==0:
  print("enter valid number")
else:
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
