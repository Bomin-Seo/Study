import urllib.request

url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
webpage = urllib.request.urlopen(url)
line = webpage.readline() # string type이 아닌 bytes type
webpage.close()

# line = line.strip()
# line = line.decode('utf-8')
# print(line)