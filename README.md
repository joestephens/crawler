# crawler
class structure for crawler with RethinkDB and Remodel ORM.

## Installation Instructions:
1. Download RethinkDB server from Rethink website
2. Start server:
..```
..rethinkdb
..```
3. In a new bash window type:
..```
..pip install remodel
..python setup.py
..```
4. Then you can launch the python repl and type the following to populate the database:
..```
..from crawler.crawler import Crawler
..
..crawler = Crawler("http://facebook.com")
..crawler.crawl()
..
..crawler = Crawler("http://google.co.uk")
..crawler.crawl()
..
..quit()
..```
5. Visit http://localhost:8080 to see the realtime read and writes, as well as the documents created.
