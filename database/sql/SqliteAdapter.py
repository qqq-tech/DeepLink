from Deeplink.database.sql import DBAdapterBase
import sqlite3


class SqliteAdapaterImpl(DBAdapterBase.AdapterBaseClass):
    def __init__(self,dbname):
        print("생성");
        self.conn(dbname)

    def __del__(self):
        self.close()
        print("파괴")

    def conn(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.conn.row_factory = lambda C, R: {c[0]: R[i] for i, c in enumerate(C.description)}
        # self.cur = self.conn.cursor()

    def close(self):
        if(self.conn!=None):
            self.conn.close()

    def select(self, sql, data={}):
        self.cur = self.conn.cursor()
        self.cur.execute(sql, data)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        self.cur.close()
        return rows

    def update(self, sql, data):
        self.cur = self.conn.cursor()
        self.cur.execute(sql, data)
        self.cur.close()
        self.conn.commit()

    def delete(self, sql, data):
        self.cur = self.conn.cursor()
        self.cur.execute(sql, data)
        self.cur.close()
        self.conn.commit()

    def insert(self, sql, data):
        self.cur = self.conn.cursor()
        self.cur.execute(sql, data)
        self.cur.close()
        self.conn.commit()

    def create(self, sql, data):
        try:
            # Save dataframe to database
            data.to_sql(name=sql, con=self.conn, if_exists='append',index=False)
            print("Saved successfully!!")
            # self.cur.execute(sql, data)
        except Exception as e:
            print(e)

        finally:
            self.conn.commit()


    def getCur(self):
        return self.cur


