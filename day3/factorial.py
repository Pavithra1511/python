def fact(num):
  if num<0:
    print('number less than zero')
  elif num==0:
    print('zero factorial is one')
  else:
      factorial=1
      for i in range(1,num+1):
       factorial=factorial*i
       print('factorial value is',factorial)
fact(6)      
         
          
