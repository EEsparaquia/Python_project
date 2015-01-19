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


plt.plot([5,6,7,8],[7,3,8,3])
plt.show()