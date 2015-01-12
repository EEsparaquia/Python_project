#! Python3 

# Scraping project Ikaro2
# For more information see
# https://www.youtube.com/watch?v=3xQTJi2tqgk&index=1
# &list=PLecLJ19BYqqYbBEUX1Rdy8cl0OJ5bka1a
#

'''
	Install the library requests &
	Install the library BeatifulSoup
	with:
		 pip install requests
		 pip install BeatifulSoup4

import requests
from bs4 import BeatifulSoup



r = requests.get("http://pythonprogramming.net")
r.content

soup = BeatifulSoup(r.content)
print soup.prettify()

soup.find_all("a") #Links

for link in soup.find_all("a"):
	print link
	print link.get("href")
	print link.text

	print link.text, link.get("href")
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)




	NEW WAY OF BRITISH HEAVY METAL

'''

import requests
from bs4 import BeautifulSoup

url = "http://pythonprogramming.net"
r = requests.get(url)
soup = BeautifulSoup(r.content)

links = soup.find_all("a") #Links

'''
for link in links:
	if "http" in link.get("href"):
		print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
'''

for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


g_data = soup.find_all("div", {"class":"info"})
# print g_data.text

for item in g_data:
	#print item.text
	print item.content
	#print item.content[0].find_all("a", {"class":"business-name"})[0].text #to see just one
	#print item.content[0].text
	#print item.content[1].text
	#print item.content[2].text
	#print item.content[3].text

for x in range(1,11):
	print(x)








