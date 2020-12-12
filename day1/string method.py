#string method
string='   hello pavi ,,....pavi'
#rstrip right strip here ,. are strip syntax:rstrip(,. along with string in the defined part)
result=string.rstrip(".,pavi")
print(result)
#rjust get the integer values in brackets
res1=string.rjust(20)
print(res1)
#join
rt='hello'
sr=','.join(rt)
print(sr)
#isidentifier
name='honey'
rest=name.isidentifier
print(rest)
#isspace
space='ioio'
result5=space.isspace()
print(result5)
#rfind return the position of character
ret=name.rfind('e')#RETURN-3
print(ret)
