print("calculator")
a=int(input("enter a value: "))
b=int(input("enter b value: "))
select=input("enter select(add/sub/mul/div): ")
if select=="add":
  result=a+b
elif select=="sub":
  result=a-b
elif select=="mul":
  result=a*b
elif select=="div":
  result=a/b
print (result)  
