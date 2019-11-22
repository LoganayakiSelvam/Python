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

