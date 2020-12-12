#x prime no
x=int(input('enter a no:'))
count=0
i=2
while(i<=x/2):
  if(x%i==0):
   count+=1
   break
i+=1
print(i)
