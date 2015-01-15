#! Python3
# Programming Tutorial
# Subprocess Module
# Try thus commands line by line
# in the python's console

import subprocess
print(''' 
 _______________________
< Handle with carefully >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
''')

# Current folder
x = subprocess.call('ls -la', shell=True)
output = subprocess.check_output('ls -la', shell=True)
y = subprocess.call('Python3 script31_2.py', shell=True)
#print(x)
#print(output)
print(y)
