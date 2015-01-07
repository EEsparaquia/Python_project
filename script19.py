#! Python3

# Programming tutorial: 
# Statistics (Mean, Standard Deviation)

import statistics

print('''
		Statistics functions in Python3
	''')


list_ex = [12,4,3,1,7,8,90,23,45,56,67,33,34,23,5]
print(list_ex,'\n')

x = statistics.mean(list_ex)
print('Mean\n',x)

x = statistics.median(list_ex)
print('Mediana\n',x)

x = statistics.mode(list_ex)
print('Mode\n',x)

x = statistics.stdev(list_ex)
print('Standard Deviation\n',x)

x = statistics.variance(list_ex)
print('Variance\n',x)