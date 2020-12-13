'open and write into file '
var=open('newfile.txt','r+')
var.write('I love Letsupgrade ')
'read the file'
var=open('newfile.txt','r+')#open file for read a file without this line it can't get the result 
print(var.read())
var.close()
'appending data into previous file created'
var=open('newfile.txt','r+')
var.write('learning needs patience ')
var.close
'again read the file'
var=open('newfile.txt','r')
print(var.read())
var.close()
#factorial
def fact(num=5):
    if num<=0:
        print('number is less than zero')
    else:
        number=num*num
        print('value is',num)

