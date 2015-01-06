#! Python3

# Programming tutorial: 
# Function Parameter Default

def simple(num1, num2):
	pass

def simple(num1, num2=5):
	print(num1,num2)

def basic_window(width, 
	height,
	font='TNR',
	color='W',
	scrollbar=True
	):
	print(width, height, font, color, scrollbar)



basic_window(500,300)

basic_window(500,300, 'a')