import requests
import psycopg2
from parser import Parser
from colour import Colour as c
from multiprocessing import Process
from database import Database

db = Database()

class MultiCrawler(object):

    def __init__(self, url):
        self.url = url
        self.parser = Parser(self.url)
        self.crawl()

    def crawl(self):
        print("%sCrawling %s%s" % (c.RED, self.url, c.EC))
        self.__get_webpage_data()
        webpage = self.parser.data

        title = webpage['title']
        url = self.url
        description = webpage['description']

        if description == "":
            print("%sSkipped.%s" % (c.ORANGE, c.EC))
            return None

        print("%s%s%s" % (c.ORANGE, title, c.EC))
        print("%s%s%s" % (c.YELLOW, url, c.EC))
        print("%s%s%s" % (c.GREEN, description, c.EC))

        db.query("INSERT into webpages (title, url, description) VALUES ('%s', '%s', '%s')" % (title[:500], url[:500], description[:500]))

        for url in webpage['urls']:
            db.query("SELECT url FROM webpages WHERE url='%s'" % (url))

            if db.cur.fetchone() == None:
                self.__new_crawling_process(url)

    def __get_webpage_data(self):
        response = requests.get(self.parser.url)
        self.parser.feed(response.text)

    def __new_crawling_process(self, url):
        if not url == self.url:
            print("Starting new process")
            process = Process(target=self.__class__, args=(url,))
            process.start()
            process.join()

        return None

crawler = MultiCrawler("http://nytimes.com/")
