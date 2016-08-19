import unittest
from crawler.parser import Parser

class TestParser(unittest.TestCase):

	def setUp(self):
		self.parser = Parser("http://google.co.uk")
		self.urls = ["http://google.co.uk", "http://news.bbc.co.uk"]

	def tearDown(self):
		pass

	def test_get_start_tag(self):
		body = '<title>'
		self.parser.feed(body)
		self.assertEqual(self.parser.data['title'], None)

	def test_get_data(self):
		body = '<title>Hey'
		self.parser.feed(body)
		self.assertEqual(self.parser.data['title'], 'Hey')

	def test_get_links(self):
		body = "<h1>Hey</h1><a href='%s'>Link 1</a><a href='%s'>Link 2</a>" % (self.urls[0], self.urls[1])
		self.parser.feed(body)
		self.assertEqual(self.parser.data['urls'], self.urls)

	def test_ignores_tags(self):
		body = "<script>some js</script><style>some css</style><h1>hey</h1>"
		self.parser.feed(body)
		self.assertEqual(self.parser.data, { 'h1': 'hey', 'webpage_urls': [] })
