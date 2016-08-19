import random

class Colour:
    EC = "\033[0m"
    RED = "\033[0;31m"
    ORANGE = "\033[0;33m"
    YELLOW = "\033[0;33;1m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34;1m"
    INDIGO = "\033[0;35m"
    VIOLET = "\033[0;35;1m"
#
# c = Colour
#
# while True:
#     print("%sCrawling http://www.google.co.uk%s" % (c.RED, c.EC))
#     print("%sResponse: 200 OK%s" % (c.YELLOW, c.EC))
#     print("%sParsing HTML...%s" % (c.ORANGE, c.EC))
#     rand = random.randint(2, 50)
#     print("%sFound %s links. Created %s new threads.%s" % (c.GREEN, rand, rand-1, c.EC))
#     print("%sINSERT INTO webpages%s" % (c.BLUE, c.EC))
#     print("%sINSERT INTO words%s" % (c.INDIGO, c.EC))
#     print("%sINSERT INTO webpages_words%s" % (c.VIOLET, c.EC))
#     print()
