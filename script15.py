#! Python3

# Programming tutorial: 
# Appending Files

print('''
	Appending Files
	Adding the next
	text:
	"New bit of 
	information"
	'''
	)

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')
print('"a" is for Append')
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()