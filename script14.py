#! Python3

# Programming tutorial: 
# Writing a File

text = 'Simple text to save\nNew Line!'

saveFile = open('/Users/ernestosamanom/Computer_Programming/Python/exampleFile.txt','w')

print('"w" is for Write')

saveFile.write(text)
saveFile.close()