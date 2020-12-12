#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dictionary={'hi':'i"m pavi',1:'school',2:'pencil'}
print('get the value for hi',dictionary.get('hi'))#get method
# 1.pop- method syntax: (key,default ,value)'''
sales={'apple':2,'banana':3,'jelly':5,5:'panner'}
popping=sales.pop('jelly')
print('pop the item:',popping)
#2.popitem - removes last item -syntax:popitem()
sales={'apple':2,'banana':3,'jelly':5,5:'panner'}
popping=sales.popitem()
print('pop the item:',popping)
#3.update-
dictionary={'hi':'i"m pavi',1:'school',2:'pencil'}
dictionary1={'sys':"computer"}# adding str value to dict
dictionary.update(dictionary1)
dictionary.update(welcome = 9)# assigning an value got error when using welcome= code
print(dictionary)
#4.fromkeys
key={'a','b','c'}
value=[2]
items=dict.fromkeys(key,value)
print(items)
value.append(3)
print(items)# mutable SO perform dict comprehension
#immutable using dict comprehension
key={'a','b','c'}
value=[2]
final={ keys:list(value) for keys in key}
'print(list(value))  return value-2'''
print(final)
value.append(6)
print(final)
#5.items-return alike as  dict_items tubles in a list
sales={'apple':2,'banana':3,'jelly':5,5:'panner'}
item=sales.items()
print(item)
#keys
sales={'apsple':2,'banana':3,'jelly':5,5:'panner'}
key=sales.keys()
print(key)
#value
sales={'apple':2,'banana':3,'jelly':5,5:'panner'}
value=sales.values()
print(value)
#setdefault  retuns the value of the item ,for the specified key=(first value) in setdefault here jelly returns 5
sales={'apsple':2,'banana':3,'jelly':5,5:'panner'}
default=sales.setdefault('jelly',7)
print(default)
