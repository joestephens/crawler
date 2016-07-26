from crawler.models.webpage import Webpage
from crawler.models.word import Word

class Crawler(object):

    COMMON_WORDS = ['and', 'on', 'before', 'the', 'because']

    WEBPAGE_BODY = "Hijack coloration nonlabeling wald fungitoxic lincs unglozed endosarcous komondor anthropophagously outstole albertville carbonnit fuchsine. Sentient semivowel ramoon vivaciousness wraac elastoplast nondisparaging reobserve dermabrasion noncomicality harmfulness tobias accordant groaner. Naif scampishness timer wemyss sheefishes pokier fleawort oileus foreconscious melon cuchulain boswellizing microcoulomb unintrusive. Gutsily racemed predetachment hayfork autonym storyteller jinnah swinge delayingly unsentineled lackerer overliberally enslaving cryptogamic. Ditchdigging banditti catchword erlina distractibility nonebullience pietas pontian inkwell striver ichinomiya stiegel paine petechiate."

    def __init__(self, webpage):
        self.webpage = webpage
        self.webpage_body = self.WEBPAGE_BODY # needs to be replaced with empty string
        self.links = []
        self.words = []

    def crawl(self):
        self._get_webpage_body() # method needs populating
        self._extract_links() # method needs populating
        self._extract_words()
        self._remove_duplicates()
        self._remove_common_words()
        self._save_to_database()

    def get_links(self):
        return self.links

    def _extract_links(self):
        # extract the links from self.webpage_body using scrapy and populate them into self.links array
        pass

    def _extract_words(self):
        self.words = self.webpage_body.split(' ')

    def _remove_duplicates(self):
        words = list(set(self.words))
        self.words = words

    def _remove_common_words(self):
        words = [word for word in self.words if word not in self.COMMON_WORDS]
        self.words = words

    def _save_to_database(self):
        saved_webpage = Webpage.create(url=self.webpage)
        word_objects = []

        for word in self.words:
            word_existing = Word.get(word=word)

            if not word_existing:
                word_object = Word.create(word=word)
            else:
                word_object = word_existing

            word_objects.append(word_object)

        saved_webpage['words'].add(*word_objects)

    def _get_webpage_body(self):
        # scrapy gets the webpage body and populates self.webpage_body
        pass
