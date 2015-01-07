#! Python3

# Programming tutorial: 
# Read from a file

readMe = open('exampleFile.txt','r').read()

print('Reading the text as is it with read:\n',readMe)

readMe = open('exampleFile.txt','r').readlines()

print('Creating Pyhon lists with readlines:\n',readMe)
