import unittest
from crawler.multi_crawler import MultiCrawler

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = MultiCrawler("tests/fixtures/website/index.html")

    def tearDown(self):
        pass

    def test_adds_to_database(self):
        assertEqual(self.crawler.database.title, 'Example Website')
        assertEqual(self.crawler.database.description, 'Rainbow Crawler is awesome')
        assertIn('tests/fixtures/website/link2/', self.crawler.database.urls)
