class CrawlerWrapper(object):

    def __init__(self, starting_point):
        self.links = [starting_point]

    def start(self):
        first_link = self.links[0]

        if not _already_crawled(first_link):
            crawler = Crawler(first_link)
            self.links.append(crawler.get_links())
            _start_threading()

    def _already_crawled(self, webpage):
        # query webpages table in database and return true if already crawled

    def _start_threading(self):
        for link in self.links:
            # self.links.delete(link)
            # create new thread on link that calls Crawler, do get_links on the instance
            # and append links to self.links and then when all threads have finished,
            # run start again

crawlers = CrawlerWrapper("http://news.bbc.co.uk")
crawlers.start()
