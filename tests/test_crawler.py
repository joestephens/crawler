import unittest
from crawler.crawler import Crawler

class TestCrawler(unittest.TestCase):
    
    def setUp(self):
        self.crawler = Crawler()
        
    def tearDown(self):
        pass
        
    def test_returns_html(self):
        html = self.crawler.get("fixtures/website/index.html")
        self.assertIn('<html>', html)
