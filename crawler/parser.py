from html.parser import HTMLParser
import requests

class Parser(HTMLParser):
	
	def __init__(self):
		HTMLParser.__init__(self)
		self.data = { 'webpage_urls': [] }
		self.last_tag = None
		self.ignore_tags = ['script', 'style', 'link', 'html', 'head', 'button', 'img', 'input', 'label']
		
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			self.data['webpage_urls'].append(attrs[0][1])
			#print(attrs[0][1])
		
		if tag not in self.ignore_tags:	
			self.data[tag] = None
			
		self.last_tag = tag
		#print(self.data)

	def handle_data(self, data):
		if self.last_tag not in self.ignore_tags:
			self.data[self.last_tag] = data
			#print(self.data)

parser = Parser()
r = requests.get("http://www.bbc.co.uk/news/election-us-2016-36990724")
parser.feed(r.text)
print(parser.data)     
