start=int(input("enter starting range: "))
end=int(input("enter ending range: "))
for i in range(start,end):
 if(i%2==0):
  print("even number",i)
 else:
  print("odd",i)
