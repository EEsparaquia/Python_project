#! Python3

# Programming tutorial: 
# Multi-line print and Dictonaries

print('''                 
        #####################
        #####################
        #                   #
        #  Starting Python3 #
        #      Scripts      #
        #                   # 
        #####################
	''')


## Dictonary delcaration 'Jaime' is the Key 
## and value is 22, need to have a unique KEY
exDict = {'Jaime':22,'Diana':24,'Ernesto':25}

print(exDict)

print(exDict['Jaime'])

## Add a new element
exDict['Tim'] = 14
print(exDict)

## Editing Tim Key
exDict['Tim'] = 15
print(exDict)

## Erease 
del exDict['Tim']
print(exDict)

ixDict = {'Alice':[22,'blonde'],'Martha':[45,'Brown'],'Jack':[11,'Red']}
print(ixDict['Jack'][1])

ixDict['Samantha']=[31,'Blonde']
ixDict['Alice']=[22,'Blonde']
print(ixDict)
