#! Python3

# Programming tutorial: 
# Build-in Functions

import math as m

print('''                 
        #####################
        #####################
        #                   #
        #  Starting Python3 #
        #      Scripts      #
        #                   # 
        #####################
	''')

## FUNCTION Absolute value |x| like in math
exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1) == exNum2:
	print('The numbers are the same')

## This function have a build in 
## command line
# help()

## FUNCTION MIN & MAX
print('\n')
exList = [2,5,7,5,3,2]
print(exList)
print(max(exList))
print(min(exList))


## FUNCTION round
print('\n')
print('Round number of:')
x = 5.345675678
print(x)
print(round(x))

## Importing math library
## using the function floor
## and ceil in x
print('\n')
print('Original value:',x)
print('Floor, round to min')
print(m.floor(x))
print('Ceil, round to max')
print(m.ceil(x))


## Coverting to another 
## type of value

print('This a String:')
exStr = '55'
print(exStr,'\n')
print('This a Integer:')
print(int(exStr),'\n')

print('This a Integer:')
exInt = 55
print(exInt,'\n')
print('This a String:')
print(str(exInt))