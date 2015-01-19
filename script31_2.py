#! Python3

# Programming tutorial: 
# Urllib Module import urllib.request
# Basicaly go to 
# 'http://pythonprogramming.net'
# and serch basics and filter the 
# <p></p> tags to extract thr content
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
#values = {'s':'basics',
 #    'submit':'Search'}

#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#req = urllib.request.Request(url, data)
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall('<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
	print(eachP)


input('Press any key to exit!')
