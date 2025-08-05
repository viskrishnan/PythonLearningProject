# list of groceries
#list are mutable

number = [1,22,333,4444,55555,666666]
print(number[3])
print(number * 3)


colors = ['red','orange', 'blue', 'black', 'green']
print(colors[0])

mix = ['ivaan', 3, 'krishnan', 5, 'vidya', 6]
print(mix[2])

empty_list=[]
print(empty_list)

empty_list = ['krishnan', 11, 33]
empty_list[0] = 'Ivaan'
print(empty_list)

game = ['football', 'tennis', 'chess']
print('cricket' in game)

# Append we can add only single value, extend we can multiple values to the list
empty_list.append('Vidya')
print(empty_list)
empty_list.extend('hari')
print(empty_list)
empty_list.remove(11)
print(empty_list)
del empty_list

li = ['Mike', 10.1,1980,10, 12]
print(li)
li.insert(2, 'pop')
print(li)
print(li.index(1980))
print(len(li))

# list slicing
num = [10,20,30,40,50,60,70]
print(num[0:5:2]) #interval is 2 here so skipping 2 numbers


x = []
for i in range(11):
    if i % 2 == 0:
        z = i ** 2
        x.append(z)
print(x)


#list comprehension
#Syntax [ expression for item in list {if expression} ]
x = [i ** 2 for i in range(11) if i ** 2 % 2 == 0 ]
print(x)