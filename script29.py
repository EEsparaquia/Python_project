#! Python3

# Programming tutorial: 
# OS Module, and Time module

import os
import time

print('''                 
        #####################
        #####################
        #                   #
        #  Stating Python3  #
        #      Scripts      #
        #                   # 
        #####################
	''')
## Equivalent to pwd linux command
curDir = os.getcwd()
print(curDir)

## Equivalent to mkdir linux command
os.mkdir('newFolder')

## Sleep the actions, time in seconds
time.sleep(2)

## Rename Directories
os.rename('newFolder','newDir')
time.sleep(2)

## Rename Directories
os.rmdir('newDir')