#for loop to print prime
for number in range(2,1001):
  count=0
  for i in range(2,(number//2+1)):
   if(number%i==0):
      count=count+1
      break
  if(count==0 and number!=1):
   print(number)

