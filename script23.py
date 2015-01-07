#! Python3

# Programming tutorial: 
# List Manipulation

x = [2,3,4,6,4,7,9,1,3,5,7,9,5]
print('Original List\n',x)

# Add information with append at the end
x.append(2)
print('Append 2\n',x)
# Add information in the index 2
# the data '99'
x.insert(2,99)
print('Insert 99 at the index 2\n',x)
# Remove the first '2' in the list
x.remove(2)
print('Remove the first 2\n',x)
# Remove the first '2' in the list by reference
x.remove(x[2])
print('Remove by reference of index\n',x)
# Acces the index 5 and the index 7
print(x[5:7])

# Print the index value of number 1
print(x.index(1))

# Acces the end of the list
print('Print the last value of the list\nx[-1]\n',x[-1])

# Count determinates values
print('Count the sixes with x.count(6)\n',x.count(6))

# Sorting the list
x.sort();
print(x)

y = ['Diana','Rocio','Aurora','Julieta','Gloria','Karina']

y.sort()
print(y)