#! Python3
# Programming Tutorial
# CX FREEZE Python to .EXE
#
# Requirements:
# 
# 1.- Install ex_Freeze from
#       www.pypi.python.org
#
# 2.- Using script31_2.py with out comments
# 3.- Make a script40_2.py called setup 

import urllib.request
import urllib.parse
import re

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

url = 'http://pythonprogramming.net'
values = {'s':'basics',
		  'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall('<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
	print(eachP)


input('Press any key to exit!')