#! Python3

# Programming tutorial
# FTP library

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

from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specficdomain-or-location/')

def grabFile():
	filename = 'fileName.txt'
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024) #1024 Buffer
	ftp.quit()
	localfile.close()

def placeFile():
	filename = 'filename.txt'
	ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
	ftp.quit()