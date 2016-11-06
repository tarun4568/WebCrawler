import HTMLParser
import urllib

urlText=[]

#Define HTMLParser

class parseText(HTMLParser.HTMLParser):
	def handle_data(self,data):
		if data != '\n':
			urlText.append(data)
			
# function to get the count of seareched keyword

def getCountOfSearchedKeyword(keyword):
	count=0
	print urlText
	for word in urlText:
		if word.find(keyword)>=0:
			count+=1
	return count

def getUrlData(url,keyword):
# creating an instance of HTMLParser
	lparser=parseText()
	#feed HTML file
	lparser.feed(urllib.urlopen(url).read())
	lparser.close()
	print "Total no of results = "+ str(getCountOfSearchedKeyword(keyword))

url='http://www.shopping.com/xCH-tv_and_video'
keyword='shop'
getUrlData(url,keyword)