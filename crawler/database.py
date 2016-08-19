import psycopg2

class Database():

    def __init__(self):
        self.conn = psycopg2.connect("dbname=varys_development")
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()
