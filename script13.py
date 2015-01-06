#! Python3

# Programming tutorial: 
# Global and Local Variables
print('''
Dont run just the script
See the code below and the
commends in it.
	''')

x = 6 

def example():
	z = 5
	print('Function 1',z)

example()


def example2():
	print('Function 2',x)

example2()

def example3():
	global x   # It cames a error if x isn't 
			   # declaire global
	z = 5
	print('Function 3',z)
	print('Function 4\n Assign ',x)
	x += 5   
	print(x)

example3()


def example4():
	print('''
		Ultimate 
		way for 
		Do It
		''')
	globx = x
	print(globx)
	globx+=5
	print(globx)

	return globx

example4()

val = 5

def example5():
	print('''
		Doing
		Propely
		''')
	glob_val = val
	print(glob_val)
	glob_val+=5
	print(glob_val)

	return glob_val

val = example5()

print(val)