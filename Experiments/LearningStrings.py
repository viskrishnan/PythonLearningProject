from sympy.physics.units import second

a = 'KrishnanTHKuMar '
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.isnumeric())
print(a.isalpha())
print(a.startswith('Krish'))
print(a.endswith('Mar'))
print(a.replace('Krish', 'Mike'))
print(a.find('nan',))
print(a)
print(a.lstrip())
print(a)
print(a.rstrip())
b = 'Mike', 'Krishnan'
print(b)
c = ','
print(c.join(b))


name = "Mike"
number = len(name)*3
print("Hello {}, your lucky number is {}.".format(name,number))

example = "format() method"
string = "This is an example of {} on a string.".format(example)
print(string)


first = "apple"
second1 = "ball"
third = "cat"
print("{0} {1} {2}".format(first,second1,third))

price = 150
with_tax = 50
print(price,with_tax)
print("Price: Rs.{:.3f}, with tax Rs.{:.2f}".format(price,with_tax))
# it can contain upto 2 float numbers that's why {:.2f}