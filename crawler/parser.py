from html.parser import HTMLParser
from urllib.parse import unquote
import requests
import re

class Parser(HTMLParser):

	def __init__(self, webpage):
		HTMLParser.__init__(self)
		self.webpage = webpage
		self.data = { 'webpage_urls': [] }
		self.last_tag = None
		self.allowed_tags = ['meta', 'title', 'h1', 'h2', 'h3', 'p']

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			url = self.__parse_url(attrs[0][1])

			if url:
				self.__add_link(url)

		if tag in self.allowed_tags:
			self.data[tag] = None

		self.last_tag = tag

	def handle_data(self, data):
		if not data.strip():
			return None

		if self.last_tag in self.allowed_tags:
			self.data[self.last_tag] = unquote(data)

	def __parse_url(self, url):
		if not (url.startswith('http') or url.startswith('/')):
			return None

		return self.__full_url(url)

	def __add_link(self, url):
		self.data['webpage_urls'].append(url)

	def __full_url(self, url):
		if not (url.startswith('http')):
			return self.__get_partial() + url

		return url

	def __get_partial(self):
		url = re.search('(http[s]?|ftp):\/?\/?([^:\/\s]+)(\/\w+)', self.webpage)
		return url.group(0)
