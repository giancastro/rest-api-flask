import psycopg2

DEC2FLOAT = psycopg2.extensions.new_type(
    psycopg2.extensions.DECIMAL.values,
    'DEC2FLOAT',
    lambda value, curs: float(value) if value is not None else None)

psycopg2.extensions.register_type(DEC2FLOAT)


class PostgreSQL(object):
    def __init__(self, host, database, user, password):
        self.db = psycopg2.connect(
            host=host, database=database, user=user,  password=password)
        self.cur = self.db.cursor()

    def execute(self, sql):
        self.cur.execute(sql)
        self.db.commit()

    def query(self, sql):
        try:
            self.cur = self.db.cursor()
            self.cur.execute(sql)
            cols = self.cur.description
            rs = self.cur.fetchall()
        except:
            return None
        return cols, rs
