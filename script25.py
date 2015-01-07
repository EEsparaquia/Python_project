#! Python3

# Programming tutorial: 
# Reading from a CSV spreadsheet

##	Example of the content of the file
##	called example.csv:
#	1/2/2014,5,8,red
#	1/3/2014,5,2,green
#	1/4/2014,9,1,blue

import csv

with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		print(row)

	print(row[0])
	print(row[0],row[1])

print('\n')
## Passing the data into separates string:
with open('example.csv') as csvfile:
	readCSV2 = csv.reader(csvfile, delimiter=',')
	dates = []
	colors = []
	for row in readCSV2:
		color = row[3]
		date = row[0]

		dates.append(date)
		colors.append(color)

	print(dates)
	print(colors)	
	WhatColor = input('What color do you wish to know the date of?')
	coldex = colors.index(WhatColor.lower()) #lower() for make all in lowercases
	print(coldex)
	theDate = dates[coldex]
	print(theDate)
	print('the date of the color',WhatColor,'is',theDate)
