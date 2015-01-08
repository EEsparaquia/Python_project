#! Python3

# Programming tutorial: 
# Sys Module copy of the script30.py 
# To see the power of this script run 
# at the command line: 
# >> python3 script30_2.py "Cool Stuff" <<
# For part 2
# >> python3 script30_2.py 5 <<



import sys
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

## Print the path
#print(sys.argv)

## len function is equivalent to length
## return the size of the string
if len(sys.argv) > 1:
	print(sys.argv[1])

# Part 2
	print(float(sys.argv[1])+5)

## With a function

#def main(arg):
#	print(arg)
#
#main(sys.argv[1])