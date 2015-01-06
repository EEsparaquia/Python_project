#! Python3

# Programming tutorial: If Statement

x = 5
y = 8
z = 5
a = 3

if x > y:
	print('"x" is greater than "y"\n')
else:
	print('"x" is less than "y"\n')


if z < y > x:
	print('"y" is greater than "z" and greater than "x"')

if z < y > x > a:
	print('"y" is greater than "z" and greater than "x"')

if z < x:
	print('"z" is less than "x"')

if z == x:
	print('z is equal to x')