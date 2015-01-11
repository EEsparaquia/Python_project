#! Python3

# Programming Tutorial:
# Parsing Web sites with re and urllib

import re
import urllib.request
import urllib.parse

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

## . Any character, * 0 or more, ? Match ) or 1 repeticions
## We need to convcert
paragraphs = re.findall('<p>(.*?)</p>', str(respData))

for eachParagraph in paragraphs:
	print(eachParagraph)
	

	appendMe = eachParagraph

	appendFile = open('parsePythonProgramming.txt', 'a')
	#print('"a" is for Append ')
	appendFile.write('\n')
	appendFile.write(appendMe)
	appendFile.close()

