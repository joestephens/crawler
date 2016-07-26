class Crawler(object):

    COMMON_WORDS = ['and', 'on', 'before', 'the', 'because']

    def __init__(self, webpage):
        self.webpage = webpage
        self.links = []

    def start(self):
        # Use scrapy to grab main content/article from webpage
        content = __scrapy_get_content()
        __extract_words(content)
        __extract_links(content)

    def get_links(self):
        return self.links

    def __extract_words(self, content):
        words = content.split(' ')

        for word in words:
            if not word in COMMON_WORDS:
                __add_word_to_db(word)

    def __add_word_to_db(self, word):
        # check if word is already in word table, if not then add it
        # insert into join table: word_id and webpage_id

    def __extract_links(self, content):
        # Use scrapy to extract links from content
        # for each link, check if it has been crawled already. If not, then add to
        # self.links, to be returned to CrawlerWrapper
