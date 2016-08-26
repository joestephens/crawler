from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.parse import unquote
import requests
import re

class Parser(HTMLParser):

	def __init__(self, url):
		HTMLParser.__init__(self)
		self.url = url
		self.data = { 'urls': [], 'description': "" }
		self.last_tag = None
		self.allowed_tags = ['title', 'h1', 'h2', 'h3', 'p']

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name, value in attrs:
				if name == "href":
					url = self.__parse_url(value)

					if url:
						self.__add_link(url)

		if tag == 'meta':
			if 'description' in attrs[0][1]:
				self.data['description'] = attrs[1][1][:250]

		if tag in self.allowed_tags:
			self.data[tag] = None

		self.last_tag = tag

	def handle_data(self, data):
		if not data.strip():
			return None

		if self.last_tag in self.allowed_tags:
			self.data[self.last_tag] = unquote(data)[:250]

	def __parse_url(self, url):
		if not (url.startswith('http') or url.startswith('/')):
			return None

		return self.__full_url(url)

	def __add_link(self, url):
		self.data['urls'].append(url)

	def __full_url(self, url):
		if not (url.startswith('http')):
			return self.__get_partial() + url

		return url

	def __get_partial(self):
		url = urlparse(self.url)
		
		if url:
			return("%s://%s" % (url.scheme, url.netloc))

		return None
