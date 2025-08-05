"""
list --> [] index value
list  = [1,2,3,4]

dictionary --> {} , key
dictionary --> {key:value, key:value......}
"""

my_dictionary = {'key1': 1, 'key2': 22, 'key3': 333, 'key4':4444, 'key5':55555}
print(my_dictionary['key5'])

mydict = {1:'a', 2:'b', 3:'c', 4:'d'}
print(mydict)
mydict[5] = 'e'
print(mydict)
del mydict[4]
print(mydict)
print(7 in mydict)
print(my_dictionary.values())
print(mydict.keys())
print(mydict.get(4), " key value 4 not found")
