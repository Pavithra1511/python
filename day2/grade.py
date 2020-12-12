#grading system
name=str(input('enter a name:'))
marks=int(input('enter a marks to check grades:'))
if marks>=80:
  print(name ,'You Scored A grade congrats')
elif marks>=70:
  print(name,'You Scored B grade congrats')
elif marks>=60:
  print(name,'You Scored C grade ')
elif marks>=50:
  print(name,'D grade try better,to score in exams')
elif marks>=40:
  print(name,'E grade')
else:
  print('failed in exms')
