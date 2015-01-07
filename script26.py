#! Python3

# Programming tutorial: 
# Reading Try and Except Errors

import csv

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

	try:		
		WhatColor = input('What color do you wish to know the date of?\n')
		if ( WhatColor in colors):

			coldex = colors.index(WhatColor.lower()) #lower() for make all in lowercases
			theDate = dates[coldex]
			print('The date of the color',WhatColor,'is',theDate)

		else:
			print('Color not found or is not a color\n')

	except Exception as e: # except NameError as e
		print(e)

	print('continuing...')
