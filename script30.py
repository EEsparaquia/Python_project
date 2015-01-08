#! Python3

# Programming tutorial: 
# Sys 

import sys

print('''                 
        #####################
        #####################
        #                   #
        #  Stating Python3  #
        #      Scripts      #
        #                   # 
        #####################
	''')

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

## Print the path
print(sys.argv)