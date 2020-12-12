#extend method to extend the list 
list1=['parrot',3,5.6,9.00,'kelly']
list2=['ginger','cat','belly']
list1.extend(list2)
print(list1)
#sort
list2.sort()
print(list2)
#insert
list2.insert(3,'trio')
print(list2)
#index -- store in variable and return index of 3
res=list1.index(3)
print(res)
#remove
list1.remove(9.00)
print(list1)
#count
res3=list1.count('kelly')
print(res3)
#pop --store in variable and return pop value of 3rd place
re=list1.pop(3)
print(re)
