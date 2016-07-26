class CrawlerWrapper(object):

    def __init__(self, starting_point):
        self.links = [starting_point]

    def start(self):
        first_link = self.links[0]

        if not __already_crawled(first_link):
            crawler = Crawler(first_link)
            self.links.append(crawler.get_links())
            __start_threading()

    def __already_crawled(self, webpage):
        # query webpages table in database and return true if already crawled

    def __start_threading(self):
        for link in self.links:
            # self.links.delete(link)
            # create new thread on link that calls Crawler, do get_links on the instance
            # and append links to self.links and then when all threads have finished,
            # run start again

crawlers = CrawlerWrapper("http://news.bbc.co.uk")
crawlers.start()
