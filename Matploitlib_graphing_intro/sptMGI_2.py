#! Python3
#
#	introduction to Matplotlib
# 	It is necessary Matplotlib from
#	www.matplotlib.org see the version
#	requirement. For Python3 use:
# 	pip3 install matplotlib


from matplotlib import pyplot as plt

def welcomeMsn (): 

	print(''' 
 _______________________
< Handle with carefully >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
''')


welcomeMsn()

#x = [5,6,7,8,0]
x = [5,6,7,8]
y = [7,3,8,3]

# To avoid the miss compare the length between the arrayas
if len(x) == len(y):
	plt.plot(x,y)

	plt.title('Epic Chart')
	plt.xlabel('X axis')
	plt.ylabel('Y axis')

	plt.show()

else:
	print('ATTENTION: The arrays of values has different lengths')