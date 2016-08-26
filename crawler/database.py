import psycopg2

class Database():

    def __init__(self):
        self.conn = psycopg2.connect("dbname=varys_development")
        self.cur = self.conn.cursor()

    def query(self, query, params=None):
        self.cur.execute(query, params)

    def close(self):
        self.cur.close()
        self.conn.close()
