# crawler
class structure for crawler with RethinkDB and Remodel ORM.

Installation Instructions:
Download RethinkDB server from Rethink website
Start server:
```
rethinkdb
```
In a new bash window:
```
pip install remodel
python setup.py
```
Then you can launch the python repl and type the following to populate the database:
```
from crawler.crawler import Crawler

crawler = Crawler("http://facebook.com")

crawler.crawl()

crawler = Crawler("http://google.co.uk")

crawler.crawl()

quit()
```
And if you visit http://localhost:8080 you can see the realtime read and writes, as well as the documents created.
