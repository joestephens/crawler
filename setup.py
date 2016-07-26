import remodel.connection
from remodel.utils import create_tables, create_indexes

from crawler.models.webpage import Webpage
from crawler.models.word import Word

create_tables()
create_indexes()
