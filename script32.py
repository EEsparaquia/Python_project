#! Python3

# Programming tutorial: 
# Regular Expressions  
# Ready to mix with script31.py
print('''              
        #####################
        #                   #
        #  Starting Python3 #
        #      Scripts.     #
        #  It's an exciting #
        # time to be alive  #
        #                   # 
        #####################
	''')

'''
	Identifiers:

	\   Is the notification character
	\d  Any number
	\D  Anything but a number
	\s  Any space
	\S  Anything but a space
	\w  Any characters
	\W  Anything but a character
	.   Any character, except for a new line
	\ b The white space around words
	\.  A period

	Modifiers:

	{1,3}  We're expecting 1-3
	+      Match 1 or more
	?      Match 0 or 1
	*      Match 0 or more
	$      Match the end of a String
	^      Matching the beginning of a String
	|      Either or ...
	[]     Range or "variance" [A-Z] = Capital from A to Z
			                  [A-Za-z] = A to Z and a to z
	{x}    Expecting "x" amount
	()     Every above then "<p>()</p>" it's say all between
		   parentesis

	White Space Characters:

	\ n new Line
	\s  space
	\ t Tab
	\e  Escape
	\ f Form feed
	\ r Return

	Dont Forget  to SCAPE:

	. + * ? [] $ ^ () {} | \ 
'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, an his grandfhater, Oscar, is 102.
'''

print(exampleString)
print('1.- Pull all the names\n2.- Pull all the ages \n')

ages = re.findall('\d{1,3}', exampleString)
names = re.findall('[A-Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
	ageDict[eachName] = ages[x]
	x+=1

print(ageDict)