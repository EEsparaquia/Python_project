#! Python3

# Programming tutorial: 
# Urllib Module 

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

## First PART

## Get the source code of google.com
'''
x = urllib.request.urlopen('http://www.google.com')
print(x.read())
print('\n')

'''

## Second PART -> Get Rquest POST
'''
## Base URL We want to visit
url = 'http://pythonprogramming.net'
## The dictonary also allows variables :)
var = 'search'
## Dictonary called values
values = {'s':'basic',
          'submit':var}

## Call the library urllib, then the method 
## parse and then the function urlencode of 
## the variable "values"
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''
## Third PART

try:
        x = urllib.request.urlopen('http://www.google.com/search?q=test')

        print(x.read())

except Exception as e:
        print(str(e))

try:
        url = 'http://www.google.com/search?q=test'
        ## Another Dictonary
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        ## We dont use print() becouse the lag of data is to big
        ## and cause troubles in the console, instead we sabe the
        ## info in a file ->

        saveFile = open('withHeaders.txt', 'w')
        ## Add some format with str() function
        saveFile.write(str(respData))
        saveFile.close()
        print('File succesfully created...\n')

except Exception as e:
        print(str(e))